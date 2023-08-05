from .base_update import BaseTargetUpdater
from sense_finance.finance.dao import *
from sense_finance.finance.common import *
from collections import defaultdict
from .industry_helper import IndustryTargetUpdateHelper



class IndustryTargetHandler2(BaseTargetUpdater):

    def __init__(self, is_init=True):
        super(IndustryTargetHandler2, self).__init__()
        self.target = None
        self.record = None
        self.is_init = is_init
        self.year_diff = 7
        self.industry_target_types = INDUSTRY_TARGET_TYPES
        self.industry_data = defaultdict(list)
        self.weight_targets = list()
        self.weight_datas = None

    def reset_data(self):
        self.company_record_map = None
        self.record_map = None
        self.industry_dao = None
        self.company_data_map = None
        self.industry_data = None
        self.target = None
        self.weight_targets = None
        self.weight_datas = None

    def clear_data(self):
        del self.industry_data
        del self.target_map
        del self.record_map
        del self.company_record_map
        del self.company_data_map
        del self.weight_datas

    def load_old_industry_data(self, target, industry_ids=None, record=None):
        self.industry_data.clear()
        items = self.industry_data_dao.select_target_industry_data(target, industry_ids, record)
        for item in items:
            self.industry_data[item.industry_id].append(item)
        sd.log_info("done load_old_industry_data size={0} for target={1} industry_ids={2}".format(len(items), target.id,
                                                                                                  len(industry_ids)))
        self.old_count = len(items)

    def get_industry_companys(self, industry_id):
        return self.industry_dao.get_industry_companys(industry_id)

    def load_weight_targets(self, model_class, query_by_record=False):
        if self.weight_targets:
            if not self.company_data_map and self.weight_datas:
                self.build_company_target_datas(self.weight_datas)
                sd.log_info("load_weight_targets with old size={0}".format(len(self.weight_datas)))
            return
        self.weight_targets = self.get_weight_targets(model_class)
        if not self.weight_targets:
            sd.log_error("no weight_targets for model_class {0}".format(model_class))
            return
        datas = self.target_data_dao.select_targets_datas(self.weight_targets, self.record_map, query_by_record)
        self.build_company_target_datas(datas)
        self.weight_datas = datas
        sd.log_info("select_targets_datas for weight_target_data size={0}".format(len(datas)))

    def load_target_data(self, target, query_by_record=False):
        for target2 in self.weight_targets:
            if target2.id == target.id:
                sd.log_info("found dup weight target for {}".format(target))
                return
        datas = self.target_data_dao.select_target_datas(target, self.record_map, query_by_record)
        sd.log_info("load_target_data size={0} for {1}".format(len(datas), target.id))
        self.build_company_target_datas(datas)

    @sd.try_catch_exception
    def update_target(self, target, thread_num=4, only_first=False, record=None):
        sd.log_info("start update_target industry target={0} only_first={1}".format(target, only_first))
        if not target.need_update_industry():
            sd.log_info("no need update_target industry for {0}".format(target.name))
            return True
        start_time = sd.get_current_second()
        self.industry_dao.load_data(target.model_class, need_first=True, only_first=only_first)
        industry_ids = self.industry_dao.get_model_class_industrys(target.model_class)
        if not industry_ids:
            sd.log_error("no industry_ids for {0}".format(target))
            return True
        self.target = target
        models = self.get_target_record_models([target])
        if ReportRecord not in models:
            models.append(ReportRecord)
        sd.log_info("update_industry_target get_target_record_models={0} for target={1} industry_ids={2}".format(models,
                                                                                                                 target.id,
                                                                                                                 len(industry_ids)))
        self.load_record_map(target, models, record)
        self.load_old_industry_data(target, industry_ids, record)
        self.load_weight_targets(target.model_class, record is not None)
        self.load_target_data(target, record is not None)
        self.industry_target_types = target.get_update_industry_mean_types()
        industry_ids = sorted(list(industry_ids))
        sd.log_info(
            "_get_target_industry_ids got {0} for target {1} industry_target_types={2}".format(len(industry_ids),
                                                                                               target,
                                                                                               self.industry_target_types))
        sd.execute_multi_core('update_target', self.update_industry, industry_ids, thread_num, True)
        sd.log_info(
            "done update_target industry for target={0} cost = {1} industry_ids={2} with old={3} new={4} update={5}".format(
                target.id,
                (sd.get_current_second() - start_time),
                len(industry_ids), self.old_count, self.new_count, self.update_count))
        self.company_data_map = None
        return True

    @sd.try_catch_exception
    def update_industry(self, industry_id):
        old_data = self.industry_data.get(industry_id)
        if old_data:
            old_data_map = {item.key(): item for item in old_data}
        else:
            old_data_map = dict()
        sd.log_info("old_data_map={0} for {1}".format(len(old_data_map), industry_id))
        company_map, record_items, data_items = self.get_industry_data(industry_id)
        if not company_map:
            sd.log_error("not found company for industry_id={}".format(industry_id))
            return
        sd.log_info(
            "get_industry_data company_map={0} record_items={1} data_items={2} for industry_id={3} old={4}".format(
                len(company_map),
                len(record_items),
                len(data_items),
                industry_id, len(old_data_map)))
        helper = IndustryTargetUpdateHelper(self.target)
        helper.update_industry_data(industry_id, old_data_map, company_map, record_items, data_items, self.record)
        sd.log_info("done update_industry for industry_id={0}".format(industry_id))
        self.update_count += len(helper.update_items)
        self.new_count += len(helper.new_items)

    def get_industry_data(self, industry_id):
        companys = self.get_industry_companys(industry_id)
        if not companys:
            return None, None, None
        company_map = {company.company_code: company for company in companys}
        record_items = list()
        data_items = list()
        for company in companys:
            records = self.company_record_map.get(company.company_code)
            if not records:
                continue
            record_items.extend(records)
            datas = self.company_data_map.get(company.company_code)
            if not datas:
                continue
            data_items.extend(datas)
        return company_map, record_items, data_items
