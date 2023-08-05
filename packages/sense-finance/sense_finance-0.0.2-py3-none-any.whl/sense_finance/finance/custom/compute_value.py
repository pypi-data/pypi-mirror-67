import sense_core as sd
from sense_finance.finance.target.base import BaseTargetComputer
from sense_finance.finance.util import *
from sense_finance.finance.common import *
from sense_finance.finance.custom.compute_industry import TargetIndustryValueComputer
import math


class CustomTargetValueComputer(BaseTargetComputer):

    def __init__(self, condition, target0, target_container, industry_container, target_express_result, year, time_type,
                 need_none=False):
        super(CustomTargetValueComputer, self).__init__()
        self.condition = condition
        self.target = target0
        self.industry_container = industry_container
        self.target_container = target_container
        self.target_express_result = target_express_result
        self.year = year
        self.time_type = time_type
        self.need_none = need_none
        self.industry_computer = TargetIndustryValueComputer(industry_container)

    def compute_value(self, return_size=False):
        items = self._get_time_data(self.target_container, self.year, self.time_type)
        if not items:
            sd.log_debug("invalid year={0} time_type={1}".format(self.year, self.time_type))
            return None
        size = 0
        for i in range(len(items)):
            item = items[i]
            val = self.compute_target(item)
            if val is not None:
                val = format_float(val, KEEP_NUMBER_SIZE)
                item.add_attr(self.target.field_key, val)
                size += 1
                if sd.is_debug():
                    sd.log_info(
                        "_compute_value field_key={0} val={1} len={2} year={3} time_type={4} item={5}".format(
                            self.target.field_key, val,
                            len(items),
                            self.year, self.time_type, item))
            elif self.need_none and not self.condition.report_record:
                item.add_attr(self.target.field_key, None)
            if self.condition.report_record:
                return val
        sd.log_debug(
            "done _compute_value year={0} time_type={1} target={2} size={3} items={4}".format(self.year, self.time_type,
                                                                                              self.target.name,
                                                                                              size,
                                                                                              len(items)))
        if return_size:
            return size
        return None

    def compute_target(self, item):
        val = self._compute_target0(self.target_express_result.express, item)
        if not val:
            return val
        if self.target.is_unit_percent():
            return val * 100
        return val

    def _convert_value(self, val, convert_type):
        if not convert_type:
            return val
        if not val:
            return val
        if val > 0:
            if convert_type == TARGET_VALUE_CONVERT_SQRT:
                return math.sqrt(val)
            return val
        if convert_type == TARGET_VALUE_CONVERT_ABS:
            return abs(val)
        if convert_type == TARGET_VALUE_CONVERT_NEGTIVE_ZERO:
            return 0
        if convert_type == TARGET_VALUE_CONVERT_SQRT:
            return None
        return val

    def _check_lost_type(self, val, lost_type):
        if val is not None:
            return 1
        if lost_type == TARGET_LOST_NONE:
            return -1
        if lost_type == TARGET_LOST_ZERO:
            return 0

    def _compute_basic_item(self, target_item, item):
        compute_target_item = ComputeTargetItem(report_time_type=self.condition.report_time_type, year=self.year,
                                                time_type=self.time_type, target_body=target_item.target_body,
                                                target_name=target_item.target_name,
                                                target_value=target_item.target_value)
        val1 = self.compute_target_item(self.condition, compute_target_item, item)
        val1 = self._convert_value(val1, target_item.convert_type)
        lost_type = self._check_lost_type(val1, target_item.lost_type)
        if lost_type == -1:
            return None, False
        if lost_type == 0:
            val1 = 0
        return val1, True

    def _compute_target_items(self, target_items, item):
        val = None
        for i, target_item in enumerate(target_items):
            if target_item.is_basic():
                val1, flag = self._compute_basic_item(target_item, item)
                if not flag:
                    return None
            elif target_item.is_composite():
                val1 = self._compute_target0(target_item, item)
            elif target_item.is_num():
                val1 = target_item.value
            else:
                return None
            if i == 0:
                val = val1
                continue
            if not target_item.operator:
                return val
            val = compute_operator_value(target_item.operator, val, val1)
        return val

    def _compute_target0(self, express, item):
        val = self._compute_target_items(express.items, item)
        if val is None:
            return None
        val = self._convert_value(val, express.convert_type)
        lost_type = self._check_lost_type(val, express.lost_type)
        if lost_type == -1:
            return None
        if lost_type == 0:
            val = 0
        return val

    def _get_time_data(self, target_container, year, time_type):
        key = get_report_time_key(year, time_type)
        return target_container.time_data_items(key)

    def _get_year_and_time_type(self, report_time_type, year, time_type, target_value):
        report_time_type1 = report_time_type
        is_year = False
        diff = get_last_period_target_value_diff(target_value)
        if diff > 0:
            if report_time_type in get_period_time_types():
                is_year = True
        else:
            diff = get_last_season_target_value_diff(target_value)
            if diff <= 0:
                diff = get_last_year_target_value_diff(target_value)
                is_year = True
        if diff <= 0:
            return year, time_type
        if is_year:
            report_time_type1 = REPORT_CYCLE_YEAR
        year1, time_type1 = get_last_time_interval(report_time_type1, year, time_type, diff)
        if sd.is_debug():
            sd.log_info(
                "_get_year_and_time_type year={0} time_type={1} for year={2} time_type={3} report_time_type={4} season_diff={5}".format(
                    year1, time_type1, year, time_type, report_time_type, diff))
        return year1, time_type1

    # 分割公司和行业两种计算逻辑
    def compute_target_item(self, condition, compute_target_item, item):
        report_time_type = compute_target_item.report_time_type
        year = compute_target_item.year
        time_type = compute_target_item.time_type
        target_body = compute_target_item.target_body
        target_name = compute_target_item.target_name
        target_value = compute_target_item.target_value
        target = self.target_express_result.get_target(target_name)
        if not target:
            sd.log_info(
                "compute_target_item not found target for name={0}".format(target_name, ))
            return None
        if target_value == TARGET_VALUE_NUMBER:
            return self._compute_target_body_value(condition, target_body, target, item, year, time_type)
        last_year, last_time_type = self._get_year_and_time_type(report_time_type, year, time_type, target_value)
        last_body_value = self._compute_last_body_value(condition, last_year, last_time_type, target_body, target_value,
                                                        item,
                                                        target)
        if sd.is_debug():
            sd.log_info(
                "compute_target_item year={0} time_type={1} target_value={2} last_body_value={3}".format(year,
                                                                                                         time_type,
                                                                                                         target_value,
                                                                                                         last_body_value))
        if is_number_target_value(target_value):
            return last_body_value
        if last_body_value is None or last_body_value == 0:
            return None
        target_body_value = self._compute_target_body_value(condition, target_body, target, item, year, time_type)
        if target_body_value is None:
            return None
        val = (target_body_value - last_body_value) * 1.0 / last_body_value
        return format_float(val, KEEP_NUMBER_SIZE)

    def _get_compare_target_num(self, target_value):
        if target_value == TARGET_VALUE_THREE_YEAR_RATIO:
            return 3
        return 1

    def _compute_last_body_value(self, condition, year, time_type, target_body, target_value, item, target):
        index = self._get_compare_target_num(target_value)
        value_list = list()
        year1 = year
        for i in range(index):
            year1 += i
            last_body_value = self._compute_company_body_value(item, condition, target, target_body, year,
                                                               time_type)
            if last_body_value is not None:
                value_list.append(last_body_value)

        if not value_list:
            return None
        if is_number_target_value(target_value):
            return value_list[0]
        last_body_value = sum(value_list) * 1.0 / len(value_list)
        return last_body_value

    def _compute_industry_body_value(self, item, condition, target, target_body, year, time_type):
        last_items = self._get_time_data(self.target_container, year, time_type)
        if not last_items:
            return None
        last_item = self.target_container.time_company_item(get_report_time_key(year, time_type), item.company_id)
        last_body_value = self._compute_target_body_value(condition, target_body, target, last_item, year,
                                                          time_type)
        return last_body_value

    def _compute_company_body_value(self, item, condition, target, target_body, year, time_type):
        last_items = self._get_time_data(self.target_container, year, time_type)
        if not last_items:
            return None
        last_item = self.target_container.time_company_item(get_report_time_key(year, time_type), item.company_id)
        last_body_value = self._compute_target_body_value(condition, target_body, target, last_item, year,
                                                          time_type)
        return last_body_value

    def _compute_target_body_value(self, condition, target_body, target, item, year, time_type):
        if not item:
            return None
        if target_body == TARGET_BODY_COMPANY:
            if not item:
                return None
            val = item.get_attr(target.field_key)
            if not val:
                return val
            if target.is_unit_percent():
                val = val / 100
            return val
        return self.industry_computer.compute_industry_body_value(item, condition, target_body, target, year, time_type)
