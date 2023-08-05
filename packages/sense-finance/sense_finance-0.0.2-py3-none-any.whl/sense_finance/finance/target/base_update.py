from collections import defaultdict
from .base import BaseTargetComputer
from .model_class import ComapnyModelClassManager
from sense_finance.finance.helper import *


class BaseTargetUpdater(BaseTargetComputer):

    def __init__(self):
        super(BaseTargetUpdater, self).__init__()
        self.model_class_manager = ComapnyModelClassManager()
        self.model_class_company_map = None
        self.target_map = dict()
        self.record_map = dict()
        self.company_record_map = defaultdict(list)
        self.company_data_map = defaultdict(list)
        self.same_count = 0
        self.update_count = 0
        self.new_count = 0
        self.delete_count = 0
        self.old_count = 0

    @sd.try_catch_exception
    def clear_data(self):
        if self.record_map:
            del self.record_map
        if self.company_record_map:
            del self.company_record_map
        if self.company_data_map:
            del self.company_data_map

    def load_record_map(self, target=None, models=None, record=None):
        if self.record_map:
            return
        self.load_records(target=target, models=models, record=record)

    def get_weight_targets(self, model_class):
        result = list()
        name_set = set()
        for target_type in get_weight_types():
            names = get_weight_row_names(target_type)
            for name in names:
                if name in name_set:
                    break
                targets = self.target_dao.find_targets_by_name(name, model_class)
                for target2 in targets:
                    if target2.model_class != model_class:
                        continue
                    result.append(target2)
                    name_set.add(name)
                    break
        return result

    def find_custom_record(self, record, custom_record_map):
        item = custom_record_map.get(record.custom_key())
        if item:
            return item
        item = self.report_data_dao.save_custom_record(record)
        custom_record_map[record.custom_key()] = item
        return item

    def load_company_custom_records(self, company_code, records=None):
        custom_record_map = dict()
        if not records:
            records = self.report_data_dao.find_company_custom_records(company_code)
        else:
            records = [item for item in records if item.is_custom()]
        for record in records:
            custom_record_map[record.custom_key()] = record
        return custom_record_map

    def load_records(self, combine_type=None, target=None, models=None, report_year=0, record=None):
        self.record_map.clear()
        self.company_record_map.clear()
        self.record_map = dict()
        self.company_record_map = defaultdict(list)
        start_time = sd.get_current_second()
        model_class = target.model_class if target else None
        if not models:
            if not target:
                models = [ReportRecord, CustomReportRecord]
            elif target.is_custom:
                models = [CustomReportRecord]
            else:
                models = [ReportRecord]
        report_time_types = None
        model_no = None
        if record:
            report_year = record.report_year
            report_time_types = [record.report_period]
            model_no = record.model_no
        records = self.target_data_dao.select_target_records(models, combine_type=combine_type,
                                                             report_time_types=report_time_types,
                                                             model_class=model_class, report_year=report_year,
                                                             model_no=model_no)
        sd.log_info(
            "select_target_records size={0} for target={1} combine_type={2} report_year={3} report_time_types={4} model_no={5} cost={6}".format(
                len(records), target, combine_type, report_year, report_time_types, model_no,(
                        sd.get_current_second() - start_time)))
        self.record_map = {record.key: record for record in records}
        for record in records:
            self.company_record_map[record.company_code].append(record)

    def load_target_data0(self, target):
        datas = self.target_data_dao.select_target_datas(target, self.record_map)
        sd.log_info(
            "load_data0 for target={0} records={1} datas={2}".format(target.id, len(self.record_map), len(datas)))
        self.build_company_target_datas(datas)
        return len(datas)

    def build_company_target_datas(self, datas):
        if not self.company_data_map:
            self.company_data_map = defaultdict(list)
        for data in datas:
            record = self.record_map[data.record_key]
            self.company_data_map[record.company_code].append(data)

    def load_targets_data(self, targets, init_data_map=True):
        start_time = sd.get_current_second()
        if init_data_map:
            self.company_data_map = defaultdict(list)
        size = 0
        for target in targets:
            size += self.load_target_data0(target)
        end_time = sd.get_current_second()
        sd.log_info("done load_data for targets={0} cost={1}".format(targets, (end_time - start_time)))
        return size

    def load_model_class_company_map(self, model_class=None):
        if not self.model_class_company_map or not self.model_class_company_map.get(model_class):
            self.model_class_company_map = self._load_model_class_company_map(model_class)
        return self.model_class_company_map.get(model_class)

    def _load_model_class_company_map(self, model_class=None):
        map = defaultdict(list)
        self._load_model_class_company_map0(map, CompanyInfo, model_class)
        return map

    def _load_model_class_company_map0(self, map, company_class, model_class=None):
        if model_class:
            items = company_class.objects.filter(model_class=model_class).all()
        else:
            items = company_class.objects.all()
        for item in items:
            if not item.model_class:
                continue
            map[item.model_class].append(item)
