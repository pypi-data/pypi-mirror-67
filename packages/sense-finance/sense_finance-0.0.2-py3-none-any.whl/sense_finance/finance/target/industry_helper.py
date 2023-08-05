import sense_core as sd
from .base import BaseTargetComputer
from sense_finance.finance.common import *
import datetime
from sense_finance.finance.model import *


class IndustryTargetUpdateHelper(BaseTargetComputer):

    def __init__(self, target):
        super(IndustryTargetUpdateHelper, self).__init__()
        self.target = target
        self.year_diff = 7
        self.update_items = list()
        self.new_items = list()
        self.industry_target_types = INDUSTRY_TARGET_TYPES

    def _build_target_data_map(self, company_map, record_items, data_items, year, time_type, combine_type):
        records = list()
        record_keys = set()
        for record in record_items:
            if record.report_year == year and record.report_period == time_type and record.report_scope == combine_type:
                records.append(record)
                record_keys.add(record.key)
        if not records:
            return None
        datas = [data for data in data_items if data.record_key in record_keys]
        return self.target_data_dao.build_industry_target_data(records, datas, company_map)

    def update_industry_data(self, industry_id, old_data_map, company_map, record_items, data_items, record=None):
        if record:
            self._update_industry_data0(industry_id, old_data_map, company_map, record_items, data_items,
                                        [record.report_period], [record.report_scope], record.report_year)
        else:
            current_year = get_current_year()
            time_types = get_all_report_time_types()
            combine_types = list(REPORT_BORE_MAP.keys())
            for year in range(current_year, current_year - self.year_diff, -1):
                self._update_industry_data0(industry_id, old_data_map, company_map, record_items, data_items,
                                            time_types,combine_types, year)
        self._save_data(industry_id, old_data_map)

    def _update_industry_data0(self, industry_id, old_data_map, company_map, record_items, data_items, time_types,
                               combine_types, year):
        for time_type in time_types:
            for combine_type in combine_types:
                target_data_map = self._build_target_data_map(company_map, record_items, data_items, year,
                                                              time_type, combine_type)
                if target_data_map is None:
                    continue
                self._save_industry_target_map(industry_id, year, time_type, combine_type, target_data_map,
                                               old_data_map)

    def _save_industry_target_map(self, industry_id, year, time_type, combine_type, target_data_map, old_data_map):
        target_weight_map = self._build_target_weight_map(target_data_map)
        for target_type in self.industry_target_types:
            self._save_industry_target_data(industry_id, year, time_type, combine_type, target_data_map,
                                            target_type, target_weight_map, old_data_map)
            # sd.log_info("done _save_industry_target_map industry_id={0} year={1} time_type={2} combine_type={3}".format(
            #     industry_id, year, time_type, combine_type))

    def _build_target_weight_map(self, target_data_map):
        model_ids = list(target_data_map.target_map.keys())
        models = ReportModel.objects.filter(id__in=model_ids).all()
        model_name_map = {model.name: model for model in models}
        result = dict()
        for weight_type in get_weight_types():
            result[weight_type] = self._get_target_weights(target_data_map, model_name_map,
                                                           weight_type)
        return result

    def _save_industry_target_data(self, industry_id, year, time_type, combine_type, target_data_map, target_type,
                                   target_weight_map, old_data_map):
        target_items = list()
        self._save_industry_target_item(self.target.id, industry_id, year, time_type, combine_type,
                                        target_data_map, target_type, target_weight_map, target_items)
        if not target_items:
            return
        if not old_data_map:
            self.new_items.extend(target_items)
            return
        for item in target_items:
            old_item = old_data_map.get(item.key())
            if old_item:
                if old_item.value == item.value:
                    continue
                old_item.value = item.value
                old_item.create_time = datetime.datetime.now()
                self.update_items.append(old_item)
            else:
                self.new_items.append(item)

    @sd.try_catch_exception
    def _save_data(self, industry_id, old_data):
        if not self.update_items and not self.new_items:
            return
        sd.log_info(
            "start _save_data industry_id={0} new={1} update={2} old={3}".format(industry_id, len(self.new_items),
                                                                                 len(self.update_items), len(old_data)))
        for item in self.update_items:
            item.save()
        if self.new_items:
            self.industry_data_dao.batch_save_industry_data(self.new_items)
        sd.log_info(
            "done _save_data industry_id={0} new={1} update={2} old={3}".format(industry_id, len(self.new_items),
                                                                                len(self.update_items), len(old_data)))

    def _save_industry_target_item(self, model_id, industry_id, year, time_type, combine_type, target_data_map,
                                   target_type, target_weight_map, target_items):
        data = target_data_map.get(model_id)
        if not data:
            return
        values = [item.value for item in data]
        if target_type == COMPARE_MEAN_SIMPLE:
            value = sum(values) * 1.0 / len(values)
        elif is_compare_weight_mean(target_type):
            target_weights = target_weight_map.get(target_type)
            if not target_weights:
                sd.log_warn(
                    "target_weights target_weights not valid target_type={4} for industry_id={0},year={1},time_type={2},combine_type={3}".format(
                        industry_id, year, time_type, combine_type, target_type))
                return
            size = 0
            total = 0
            for item in data:
                weight = target_weights.get(item.company_id)
                if not weight:
                    continue
                size += 1
                total += weight * item.value
            if size == 0:
                sd.log_warn(
                    "_save_industry_target_data size 0 target_type={4} for industry_id={0},year={1},time_type={2},combine_type={3}".format(
                        industry_id, year, time_type, combine_type, target_type))
                return
            value = total
        else:
            values.sort()
            if target_type == INDUSTRY_TARGET_MAX:
                value = values[len(values) - 1]
            elif target_type == INDUSTRY_TARGET_MIN:
                value = values[0]
            elif target_type == INDUSTRY_TARGET_MIDDLE:
                middle = int(len(values) / 2)
                if len(values) % 2 == 1:
                    value = values[middle]
                else:
                    value = (values[middle] + values[middle - 1]) * 1.0 / 2
            else:
                return
        value = format_float(value, KEEP_NUMBER_SIZE)
        item = IndustryTargetData(report_scope=combine_type, report_period=time_type, report_year=year,
                                  report_model_id=model_id, target_type=target_type,
                                  industry_id=industry_id, value=value, create_time=datetime.datetime.now())
        target_items.append(item)

    def _get_target_weights(self, target_data_map, model_name_map, target_type):
        names = get_weight_row_names(target_type)
        for name in names:
            model = model_name_map.get(name)
            if not model:
                continue
            data = target_data_map.get(model.id)
            if not data:
                continue
            total = 0
            for item in data:
                total += abs(item.value)
            if total <= 0:
                continue
            return {item.company_id: abs(item.value) * 1.0 / total for item in data}
        return None
