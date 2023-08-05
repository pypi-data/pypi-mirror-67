from sense_finance.finance.common import *
from sense_finance.finance.helper import *
from sense_finance.finance.model import *
from sense_finance.finance.dao.company import CompanyDAO


class IndustryDAO(object):

    def __init__(self, industry_ids=None):
        self.industry_ids = industry_ids
        self.industry_company_map = defaultdict(list)
        self.model_class_industry_map = defaultdict(set)

    def _is_valid_industry(self, industry_id):
        if not self.industry_ids:
            return True
        return industry_id in self.industry_ids

    def reload_data(self, model_class=None, need_first=True, only_first=False):
        self.industry_company_map = defaultdict(list)
        self.model_class_industry_map = defaultdict(set)
        company_dao = CompanyDAO()
        companys = company_dao.get_finance_all(model_class=model_class, filter_dup=True)
        for company in companys:
            if not self._is_valid_industry(company.first_industry_code):
                continue
            if company.first_industry_code and need_first:
                self.industry_company_map[company.first_industry_code].append(company)
                if company.model_class:
                    self.model_class_industry_map[company.model_class].add(company.first_industry_code)
            if only_first:
                continue
            if not self._is_valid_industry(company.second_industry_code):
                continue
            if company.second_industry_code:
                self.industry_company_map[company.second_industry_code].append(company)
                if company.model_class:
                    self.model_class_industry_map[company.model_class].add(company.second_industry_code)
            if company.three_industry_code:
                self.industry_company_map[company.three_industry_code].append(company)
                if company.model_class:
                    self.model_class_industry_map[company.model_class].add(company.three_industry_code)
            if company.four_industry_code:
                self.industry_company_map[company.four_industry_code].append(company)
                if company.model_class:
                    self.model_class_industry_map[company.model_class].add(company.four_industry_code)
        sd.log_info(
            "done reload_data industry model_class={0}, need_first={1}, only_first={2} industry_company_map={3}".format(
                model_class, need_first,
                only_first, len(self.industry_company_map)))

    def load_data(self, model_class=None, need_first=False, only_first=False):
        if self.industry_company_map:
            return
        self.reload_data(model_class, need_first, only_first)

    def get_industry_companys(self, industry_id):
        return self.industry_company_map.get(industry_id)

    def get_model_class_industrys(self, model_class):
        return self.model_class_industry_map.get(model_class)


class IndustryDataDAO(object):

    def select_target_industry_data(self, target, industry_ids=None, record=None):
        times = 5
        while times >= 0:
            times -= 1
            try:
                sd.log_info("start select_target_industry_data target={0}".format(target.id))
                time = sd.get_current_second()
                objects = IndustryTargetData.objects.filter(report_model_id=target.id)
                if record:
                    objects = objects.filter(report_scope=record.report_scope, report_year=record.report_year,
                                             report_period=record.report_period)
                    if industry_ids:
                        objects = objects.filter(industry_id__in=industry_ids)
                items = objects.all()
                sd.log_info(
                    "done select_target_industry_data size={0} target={1} cost={2}".format(len(items), target.id,
                                                                                           sd.get_current_second() - time))
                return items
            except Exception as ex:
                sd.log_exception(ex)
                sd.sleep(2)
        raise Exception("select_target_industry_data failed for target={}".format(target.id))

    def select_industry_data(self, industry_id, targets=None):
        objects = IndustryTargetData.objects.filter(industry_id=industry_id)
        if targets:
            model_ids = [target.id for target in targets]
            if len(model_ids) == 1:
                objects = objects.filter(report_model_id=model_ids[0])
            else:
                objects = objects.filter(report_model_id__in=model_ids)
        return objects.all()

    def delete_industry_data(self, industry_id, targets=None):
        if targets:
            model_ids = [target.id for target in targets]
            IndustryTargetData.objects.filter(industry_id=industry_id, report_model_id__in=model_ids).delete()
        else:
            model_ids = None
            IndustryTargetData.objects.filter(industry_id=industry_id).delete()
        sd.log_info("done delete IndustryTargetData for {0} model_ids={1}".format(industry_id, model_ids))

    @sd.try_catch_exception
    def batch_save_industry_data(self, items):
        IndustryTargetData.objects.bulk_create(items, batch_size=100)
        sd.log_info("batch_save_industry_data size={}".format(len(items)))

    def select_data(self, condition):
        result = IndustryTargetDataMap()
        targets = condition.get_select_field_targets()
        if targets:
            self._select_data0(condition, targets, IndustryTargetData, result)
        sd.log_info("select industry size={0} for {1} targets={2}".format(len(result), condition, len(targets)))
        return result

    def select_single_data_item(self, condition):
        return IndustryTargetData.objects.filter(
            industry_id=condition.industry_id, report_scope=condition.combine_type,
            report_year=condition.start_year,
            report_period=condition.report_time_type, report_model_id=condition.compare_target.id,
            target_type=condition.compare_type).first()

    def _select_data0(self, condition, targets, model_class, result):
        industry_id = condition.industry_id
        model_ids = [x.id for x in targets]
        sd.log_info(
            "_select_data0 industry model_ids={0},report_period__in={1},industry_id={2},compare_type={3},start_year={4},end_year={5},model_class={6}".format(
                model_ids, get_report_time_types(
                    condition.report_time_type), industry_id, condition.compare_type, condition.select_start_year,
                condition.select_end_year, model_class))
        objects = model_class.objects.filter(
            industry_id=industry_id,
            report_scope=condition.combine_type,
            report_period__in=get_report_time_types(condition.report_time_type),
            report_year__gte=condition.select_start_year,
            report_year__lte=condition.select_end_year,
            report_model_id__in=model_ids)
        if type(condition.compare_type) == list:
            records = objects.filter(target_type__in=condition.compare_type).all()
        else:
            records = objects.filter(target_type=condition.compare_type).all()

        target_map = {target.id: target for target in targets}
        for item in records:
            result.add(target_map[item.report_model_id].field_key, item)
        return records

    def select_industry_items(self, report_model_id, target_types=None):
        last_id = 0
        limit = 1000 if sd.is_debug() else 5000
        result = list()
        while True:
            items = list(IndustryTargetData.objects.filter(report_model_id=report_model_id).filter(
                id__gt=last_id).order_by('id').all()[0:limit])
            if not items:
                break
            last_id = items[len(items) - 1].id
            item_size = len(items)
            if target_types:
                items = [item for item in items if item.target_type in target_types]
            result.extend(items)
            if item_size < limit:
                break
        sd.log_info(
            "select_industry_data_result result size={0} for report_model_id={1} target_types={2}".format(
                len(result), report_model_id, target_types))
        return result

    def load_industry_data_container(self, report_model_id_map):
        container = IndustryTargetDataContainer()
        for report_model_id, target_types in report_model_id_map.items():
            items = self.select_industry_items(report_model_id, target_types)
            if items:
                container.extend(items)
        return container
