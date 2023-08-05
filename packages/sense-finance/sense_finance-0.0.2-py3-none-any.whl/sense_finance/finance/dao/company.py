from sense_finance.finance.model import *
from django.db.models import Q
from sense_finance.finance.common import *


class CompanyDAO(object):

    def find_all_sense_companys(self):
        return list(CompanyInfo.find_all())

    def is_same_company(self, company1, company2):
        if company1.company_full_name and company1.company_full_name == company2.company_full_name:
            return True
        if company1.social_credit_code and company1.social_credit_code == company2.social_credit_code:
            return True
        return False

    def filter_dup_company_items(self, company_list, need_credit_code=False):
        keys = set()
        items = list()
        for company in company_list:
            if need_credit_code and not company.social_credit_code:
                continue
            if company.social_credit_code in keys or company.company_full_name in keys:
                continue
            if company.social_credit_code:
                keys.add(company.social_credit_code)
            keys.add(company.company_full_name)
            items.append(company)
        return items

    def get_model_classes(self):
        items = list(CompanyInfo.objects.values_list('model_class', flat=True).distinct())
        return [item for item in items if item]

    def get_by_company_code(self, company_code):
        result = self.gets_by_company_codes([company_code])
        if not result:
            return None
        return result[0]

    def _gets_by_social_credit_codes0(self, codes, model):
        if len(codes) == 1:
            return list(model.objects.filter(social_credit_code=codes[0]).all())
        result = list()
        unit = 1000
        total = len(codes)
        for i in range(int(total / unit) + 1):
            if i * unit >= total:
                break
            if total < (i + 1) * unit:
                ids = codes[i * unit:total]
            else:
                ids = codes[i * unit:(i + 1) * unit]
            items = model.objects.filter(social_credit_code__in=ids).all()
            result.extend(list(items))
        sd.log_info(
            "_gets_by_social_credit_codes0 size={0} for codes {1}".format(len(result), len(codes)))
        return result

    def get_by_social_credit_code(self, code):
        items = self.gets_by_social_credit_code(code)
        return items[0] if items else None

    def gets_by_social_credit_code(self, code):
        items = self.gets_by_social_credit_codes([code])
        return items

    def gets_by_social_credit_codes(self, codes):
        items = self._gets_by_social_credit_codes0(codes, CompanyInfo)
        return items

    def gets_by_company_codes(self, codes):
        result = list()
        unit = 1000
        total = len(codes)
        for i in range(int(total / unit) + 1):
            if i * unit >= total:
                break
            if total < (i + 1) * unit:
                ids = codes[i * unit:total]
            else:
                ids = codes[i * unit:(i + 1) * unit]
            items = CompanyInfo.objects.filter(company_code__in=ids).all()
            result.extend(list(items))
        sd.log_info(
            "gets_by_company_codes size={0} for codes {1}".format(len(result), len(codes)))
        return result

    def get_all_company_list(self, model_class=None):
        if model_class:
            return list(CompanyInfo.objects.filter(model_class=model_class).all())
        else:
            return list(CompanyInfo.find_all())

    def get_by_model_class_industry_id(self, model_class, industry_id):
        item = CompanyInfo.objects.filter(model_class=model_class).filter(
            Q(first_industry_code=industry_id) | Q(second_industry_code=industry_id) | Q(
                four_industry_code=industry_id) | Q(
                three_industry_code=industry_id)).first()
        return item

    def get_company_by_name(self, company_name):
        info = CompanyInfo.find_one(company_full_name=company_name)
        return info

    def get_company(self, company_code):
        return CompanyInfo.find_one(company_code=company_code)

    def get_finance_all(self, uid='', model_class=None, filter_dup=False):
        return self.get_all(uid, model_class, use_model_class=True, filter_dup=filter_dup, need_credit_code=False)

    """
        默认返回所有公司，不做任何条件限制。可支持的限制是：是否有model_class，是否过滤，过滤时是否需要信用代码
        如果model_class存在，则use_model_class会忽略
        filter_dup使用时，need_credit_code判断是否需要过滤信用代码
    """
    def get_all(self, uid='', model_class=None, use_model_class=False, filter_dup=False, need_credit_code=False):
        items = self.get_all_company_list(model_class)
        sd.log_info("get_all total company size={0} for uid={1}".format(len(items), uid))
        if use_model_class and not model_class:
            items = self.filter_no_model_class_company_items(items)
        if filter_dup:
            items = self.filter_dup_company_items(items, need_credit_code)
        return items

    def filter_no_model_class_company_items(self, items):
        return [item for item in items if item.model_class]

    def gets_by_industry_id(self, industry_id, uid='', use_model_class=False):
        items = list(
            CompanyInfo.objects.filter(
                Q(first_industry_code=industry_id) | Q(second_industry_code=industry_id) | Q(
                    four_industry_code=industry_id) | Q(
                    three_industry_code=industry_id)).filter(model_class__isnull=False).all())
        return items


class FinanceCompanyDAO(object):

    def __init__(self):
        self.company_dao = CompanyDAO()

    def get_targets_industry_ids(self, targets):
        model_class_items = list(set([target.model_class for target in targets]))
        items = CompanyModelClass.find_many(model_class__in=model_class_items)
        comapny_list = self.company_dao.get_finance_all()
        comapny_map = {comapny.company_code: comapny for comapny in comapny_list}
        industry_ids = set()
        for item in items:
            comapny = comapny_map.get(item.id)
            if not comapny:
                sd.log_error("null company for {}".format(item.id))
                continue
            self._add_industry_id(industry_ids, comapny)
        sd.log_info(
            "get_targets_industry_ids {0} model_class={1} comapny size={2}".format(len(industry_ids), model_class_items,
                                                                                   len(items)))
        return industry_ids

    def get_industry_ids(self, company_list=None):
        if not company_list:
            company_list = self.company_dao.get_finance_all()
        industry_ids = set()
        for item in company_list:
            self._add_industry_id(industry_ids, item)
        industry_ids = list(industry_ids)
        return industry_ids

    def _add_industry_id(self, industry_ids, item):
        if item.first_industry_code and item.first_industry_code.strip():
            industry_ids.add(item.first_industry_code.strip())
        if item.second_industry_code and item.second_industry_code.strip():
            industry_ids.add(item.second_industry_code.strip())
        if item.four_industry_code and item.four_industry_code.strip():
            industry_ids.add(item.four_industry_code.strip())
        if item.three_industry_code and item.three_industry_code.strip():
            industry_ids.add(item.three_industry_code.strip())
