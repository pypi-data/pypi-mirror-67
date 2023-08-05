from .industry_handler import IndustryTargetHandler2
from sense_finance.finance.dao import *
from sense_finance.finance.common import *
from sense_finance.finance.model import *
import gc



class IndustryTargetUpdater(IndustryTargetHandler2):

    def __init__(self, only_first=False):
        super(IndustryTargetUpdater, self).__init__()
        self.weight_target_data_map = dict()
        self.weight_target_map = dict()
        self.only_first = only_first

    @sd.try_catch_exception
    def update_target_id(self, id, thread_num=1):
        self.update_target(TargetDAO().find_target(id), thread_num)

    def _check_record_targets(self, record, target):
        if target:
            return [target]
        datas = record.report_datas
        if not datas:
            return None
        target_ids = [data.report_model_id for data in datas]
        targets = self.target_dao.find_targets_by_ids(target_ids)
        return targets

    @sd.try_catch_exception
    def update_record(self, record, target=None):
        company = self.company_dao.get_by_company_code(record.company_code)
        if not company:
            sd.log_error("not found company for {}".format(record))
            return
        industry_ids = company.industry_ids()
        if not industry_ids:
            sd.log_info("no industry_ids for {}".format(record))
            return
        targets = self._check_record_targets(record, target)
        sd.log_info("start industry update_record target={}".format(len(targets)))
        if not targets:
            sd.log_info("not found target for record {}".format(record))
            return
        handler = IndustryTargetHandler2()
        handler.record = record
        handler.industry_dao.industry_ids = industry_ids
        # target 需要是同一种类型的，也就是或者都是基础类型或者都是自定义的
        old_count = 0
        for target in targets:
            handler.update_target(target, thread_num=1, record=record)
            old_count += handler.old_count
        sd.log_info(
            "done industry update_record target size={0} old={1} new={2} update={3}".format(len(targets), old_count,
                                                                                       handler.new_count,
                                                                                       handler.update_count))

    @sd.try_catch_exception
    def update_target(self, target, thread_num=1, record=None):
        handler = IndustryTargetHandler2()
        flag = handler.update_target(target, thread_num, self.only_first, record=record)
        handler.clear_data()
        del handler
        return flag

    @sd.try_catch_exception
    def update_target0(self, target, thread_num=4):
        close_model_connection()
        handler = IndustryTargetHandler2()
        handler.company_record_map = self.company_record_map
        handler.record_map = self.record_map
        handler.industry_dao = self.industry_dao
        handler.update_target(target, thread_num, self.only_first)
        handler.reset_data()

    @sd.try_catch_exception
    def update_all(self, only_custom=False, mod_index=1, mod_size=1, report_year=0):
        start_time = sd.get_current_second()
        sd.log_info("start update_all industry targets mod_index={0} mod_size={1}".format(mod_index, mod_size))
        self.industry_dao.reload_data(only_first=self.only_first)
        self.load_records(report_year=report_year)
        self.load_weight_targets0()
        targets = self.get_targets(only_custom)
        sd.log_info("get target size={0}".format(len(targets)))
        if mod_size > 1:
            targets = [target for target in targets if target.id % mod_size == mod_index]
        sd.log_info("get target real size={0} mod_index={1} mod_size={2}".format(len(targets), mod_index, mod_size))
        time = sd.get_current_second()
        for i, target in enumerate(targets):
            self.update_target0(target, 1)
            sd.log_info("done update_target0 for target={0} index={1} total={2}".format(target.id, i, len(targets)))
            gc.collect()
            if sd.get_current_second() > time + 3600 * 8:
                self.industry_dao.reload_data(only_first=self.only_first)
                self.load_records()
                time = sd.get_current_second()
        sd.log_info("done update_all industry targets cost {0} size={1}".format(sd.get_current_second() - start_time,
                                                                                len(targets)))

    def load_weight_targets0(self):
        sd.log_info("start load_weight_targets")
        start_time = sd.get_current_second()
        model_class_items = self.company_dao.get_model_classes()
        for model_class in model_class_items:
            weight_targets = self.get_weight_targets(model_class)
            if not weight_targets:
                sd.log_error("no weight_targets for model_class {0}".format(model_class))
                continue
            datas = self.target_data_dao.select_targets_datas(weight_targets, self.record_map)
            self.weight_target_map[model_class] = weight_targets
            self.weight_target_data_map[model_class] = datas
        sd.log_info("done load_weight_targets cost {}".format(sd.get_current_second() - start_time))

    def get_targets(self, only_custom=False):
        targets1 = CustomTarget.find_all()
        targets1 = [target for target in targets1 if target.need_update_industry()]
        if only_custom:
            return targets1
        targets = list(ReportModel.find_all())
        targets.extend(targets1)
        return targets
