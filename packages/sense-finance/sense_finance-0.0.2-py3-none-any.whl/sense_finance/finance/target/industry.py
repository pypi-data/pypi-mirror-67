from .base import BaseTargetComputer
from sense_finance.finance.helper import *
from .industry_mean import IndustryMeanComputer
from .industry_candidate2 import IndustryCandidateComputer2
from sense_finance.finance.common import *
from sense_finance.finance.helper import TargetCondition


class IndustryCompanyTargetComputer(BaseTargetComputer):

    @sd.catch_raise_exception
    def compute(self, condition):
        result = dict()
        time_range_type = get_lastest_time_range_type(condition.report_time_type)
        condition1 = TargetCondition(report_time_type=condition.report_time_type,
                                     time_range_type=time_range_type, industry_id=condition.industry_id,
                                     compare_type=condition.compare_type, limit_type=condition.limit_type,
                                     company=condition.company, compare_target=condition.compare_target,
                                     targets=[], company_list=condition.company_list,
                                     combine_type=condition.combine_type)
        condition1.ratio_type = condition.ratio_type
        candidate_computer = IndustryCandidateComputer2()
        candidates = candidate_computer.compute(condition1)
        sd.log_info("candidates={0} size={1}".format(candidates, len(candidates)))
        result['company_targets'] = self._compute_company_targets(condition, candidates)
        result['target_header'] = self.build_target_header(condition)
        compare_types = [COMPARE_MEAN_SIMPLE,
                         INDUSTRY_TARGET_MAX,
                         INDUSTRY_TARGET_MIDDLE,
                         INDUSTRY_TARGET_MIN]
        condition2 = TargetCondition(report_time_type=condition.report_time_type,
                                     time_range_type=condition.time_range_type,
                                     compare_type=compare_types, limit_type=condition.limit_type,
                                     company=condition.company, compare_target=condition.compare_target,
                                     targets=condition.targets, company_list=condition.company_list,
                                     combine_type=condition.combine_type, industry_id=condition.industry_id)
        condition2.select_start_year = condition.select_start_year
        print(condition2.select_start_year)
        mean_computer = IndustryMeanComputer()
        result['industry_targets'] = mean_computer.compute(condition2, self.report_time_items,
                                                           self.report_select_time_items)
        return result

    def _compute_company_targets(self, condition, candidates):
        result = list()
        if not candidates:
            return result
        ratio_type = condition.ratio_type
        condition2 = TargetCondition(report_time_type=condition.report_time_type,
                                     time_range_type=condition.time_range_type,
                                     compare_type=condition.compare_type, limit_type=condition.limit_type,
                                     company=condition.company, compare_target=None,
                                     targets=condition.targets, company_list=condition.company_list,
                                     combine_type=condition.combine_type, check_year_range=condition.check_year_range)
        if condition2.report_time_type == REPORT_CYCLE_YEAR:
            condition2.select_start_year -= 1
        sd.log_info("industry _compute_company_targets end_year={0} start_year={1} check_year_range={2}".format(
            condition2.select_end_year,
            condition2.select_start_year, condition2.check_year_range))
        condition2.ratio_type = ratio_type
        condition2.company_ids = [item['company_id'] for item in candidates]
        target_container = self.target_data_dao.select_target_result(condition2)
        self.build_report_time_items(condition2, target_container)
        condition.select_start_year = condition2.select_start_year
        target_result = self._parse_company_target_result(condition2, target_container)
        company_map = {x.company_code: x for x in condition2.company_list}
        for item in candidates:
            company_id = item['company_id']
            company = company_map.get(company_id)
            if not company:
                sd.log_error(
                    "not found company for {0} with condition={1} company_map={2}".format(company_id, condition2,
                                                                                          company_map.keys()))
                continue
            result.append({
                'company_name': company.company_full_name,
                'rank': item['rank'],
                'items': target_result[company_id]
            })
        return result

    def _parse_company_target_result(self, condition, target_container):
        result = {code: list() for code in condition.company_ids}
        for target in condition.targets:
            company_target_map = self._build_company_target_map(target, result, target_container)
            if condition.ratio_type == 1:
                company_target_map2 = self._build_company_target_map(target, result, target_container, 1)
            else:
                company_target_map2 = None
            self._convert_target_result(target, company_target_map, result, company_target_map2)
        return result

    def _build_company_target_map(self, target, result, target_container, year_diff=0):
        company_target_map = dict()
        for k in result.keys():
            company_target_map[k] = list()

        for time_item in self.report_select_time_items:
            year, time_type = time_item
            year -= year_diff
            key = get_report_time_key(year, time_type)
            items = target_container.time_data_items(key)
            if not items:
                item_map = dict()
            else:
                item_map = {item.company_id: item for item in items}

            for k in company_target_map.keys():
                item = item_map.get(k)
                if not item or item.get_attr(target.field_key) is None:
                    company_target_map[k].append(INVALID_TARGET_DATA)
                else:
                    company_target_map[k].append(item.get_attr(target.field_key))

        return company_target_map

    def _convert_target_result(self, target, company_target_map, result, company_target_map2):
        # 输出结构
        for k in company_target_map.keys():
            items = company_target_map[k]
            if company_target_map2 is None:
                ratio_items = None
            else:
                ratio_items = company_target_map2[k]
            items2 = list()
            for i in range(len(self.report_time_items)):
                val = items[i]
                if ratio_items is None:
                    val2 = items[i + 1]
                else:
                    val2 = ratio_items[i]
                way, ratio = self.get_target_value_way_ratio(val, val2)
                items2.append({
                    'way': way,
                    'ratio': ratio,
                    'native_value': convert_target_show_value(target, val),
                    'value': convert_target_normal_value(target, val)
                })
            result[k].append({
                'name': show_target_name(target),
                'items': items2
            })

    def build_target_header(self, condition):
        result = list()
        if not self.report_time_items:
            return result
        for target in condition.targets:
            time_items = list()
            for time_item in self.report_time_items:
                year, time_type = time_item
                time = get_show_report_time(condition.report_time_type, year, time_type)
                time_items.append(time)
            result.append({
                'name': show_target_name(target),
                'desc': build_target_desc(target),
                'time_items': time_items
            })
        return result
