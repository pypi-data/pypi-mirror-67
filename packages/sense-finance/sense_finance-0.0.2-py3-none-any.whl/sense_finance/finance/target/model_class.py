from sense_finance.finance.model import *
import sense_core as sd
from .base import BaseTargetComputer
from django.db.models import Q


class ComapnyModelClassManager(BaseTargetComputer):

    def __init__(self):
        super(ComapnyModelClassManager, self).__init__()
        self._map = dict()

    def get(self, company_code):
        item = self._map.get(company_code)
        if not item or (sd.get_current_second() - item.update_time) > 3600 * 12:
            item = self._load(company_code)
            if item:
                item.update_time = sd.get_current_second()
                self._map[item.id] = item
        return item

    # 需要修改
    def get_model_class_by_industry_id(self, industry_id):
        item = CompanyModelClass.objects.filter(Q(parent_industry_id=industry_id) | Q(industry_id=industry_id)).first()
        if item:
            return item.model_class
        return None

    def get_model_class(self, company_code, use_company=True):
        item = self.get(company_code)
        if item:
            return item.model_class
        if not use_company:
            return None
        company = self.company_dao.get_company(company_code)
        if company:
            return company.model_class

    def _load(self, company_code):
        item = CompanyModelClass.find_by_id(company_code)
        if item:
            sd.log_info("_load CompanyModelClass done for {0} get {1}".format(company_code, item))
            return item
        company = self.company_dao.get_company(company_code)
        if not company:
            return None
        return self.update(company)

    @sd.try_catch_exception
    def update(self, company):
        return self._update_model_class(company)

    def _update_model_class(self, company, record=None):
        company_code = company.company_code
        if not record:
            record = self.report_data_dao.find_latest_record(company_code)
            if not record:
                # sd.log_error("not found ReportRecord for company_code={}".format(company_code))
                return None
        if not record.model_class:
            sd.log_error("invalid model_class for record={}".format(record))
            return None
        item = self._update_company_model_class(company, record)
        if company.model_class != record.model_class:
            sd.log_info(
                "update company info model_class={0} old={1} for {2}".format(record.model_class, company.model_class,
                                                                             company_code))
            if is_sensedeal_company(company.company_code):
                company.model_class = record.model_class
                company.save()
        return item

    def _update_company_model_class(self, company, record):
        company_code = company.company_code
        item = CompanyModelClass.find_by_id(company_code)
        if not item:
            item = CompanyModelClass(id=company_code, model_class=record.model_class, industry_id=company.industry_id,
                                     industry_name=company.industry_name, parent_industry_id=company.parent_industry_id,
                                     parent_industry_name=company.parent_industry_name,
                                     update_time=sd.get_current_second())
            item.save()
            sd.log_info("_update_model_class save {}".format(item))
            return item

        if item.model_class == record.model_class:
            return item
        item.model_class = record.model_class
        item.industry_id = company.industry_id
        item.industry_name = company.industry_name
        item.parent_industry_id = company.parent_industry_id
        item.parent_industry_name = company.parent_industry_name
        item.update_time = sd.get_current_second()
        item.save()
        sd.log_info("_update_model_class update {}".format(item))
        return item

    @sd.try_catch_exception
    def check_model_class(self, record):
        if not record.model_class:
            return
        company = self.company_dao.get_company(record.company_code)
        if not company or company.model_class:
            return
        self._update_model_class(company, record)
        sd.log_info("done check_model_class for {}".format(record))

    def update_all(self):
        items = self.company_dao.find_all_sense_companys()
        sd.log_info("get update_all CompanyModelClass size={}".format(len(items)))
        sd.execute_multi_core("update_model_class", self.update, items, 1, True)
        sd.log_info("done update_all CompanyModelClass")

    def load_all(self):
        items = CompanyModelClass.objects.all()
        sd.log_info("load_all CompanyModelClass size={0}".format(len(items)))
        self._map = dict()
        for item in items:
            item.update_time = sd.get_current_second()
            self._map[item.id] = item
