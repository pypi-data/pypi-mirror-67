from sense_finance.finance.model import *
from collections import OrderedDict
from sense_finance.finance.target import ComapnyModelClassManager
from sense_finance.finance.common import *
from sense_finance.finance.dao import *


class BaseFinanceService(object):

    @classmethod
    def build_company_industry_ranges(cls, company_code):
        dao = CompanyDAO()
        company = dao.get_company(company_code)
        industry_list = list()
        if not company:
            return industry_list
        if company.first_industry_code:
            industry_list.append({'name': '一级', 'value': company.first_industry_code})
        if company.second_industry_code:
            industry_list.append({'name': '二级', 'value': company.second_industry_code})
        if company.three_industry_code:
            industry_list.append({'name': '三级', 'value': company.three_industry_code})
        if company.four_industry_code:
            industry_list.append({'name': '四级', 'value': company.four_industry_code})
        return industry_list

    @classmethod
    def check_param_industry_range(cls, params, info):
        industry_range = params.get('industry_range')
        if not industry_range:
            params['industry_range'] = info.industry_id
        elif industry_range != info.first_industry_code and industry_range != info.second_industry_code and industry_range != info.three_industry_code and industry_range != info.four_industry_code:
            sd.log_info(
                "change industry_range from {0} to {1} second_industry_code={2} three_industry_code={3} four_industry_code={4}".format(
                    params['industry_range'], info.industry_id, info.second_industry_code, info.three_industry_code,
                    info.four_industry_code))
            params['industry_range'] = info.industry_id
        return params['industry_range']

    @classmethod
    def compress_menu_data(cls, result):
        company_industry_tree = result.get('company_industry_tree')
        if company_industry_tree:
            cls._company_industry_tree_items(company_industry_tree)

    @classmethod
    def _company_industry_tree_items(cls, items):
        for item in items:
            item['c'] = item['code']
            item['n'] = item['name']
            item['i'] = item['index']
            item['py'] = item['pin_yin']
            del item['code']
            del item['name']
            del item['index']
            del item['pin_yin']
            if 'companys' in item:
                companys = item['companys']
                for company in companys:
                    company['c'] = company['company_code']
                    company['n'] = company['company_name']
                    company['i'] = company['in_industry']
                    company['s'] = company['is_stock']
                    company['py'] = company['pin_yin']
                    del company['company_code']
                    del company['company_name']
                    del company['in_industry']
                    del company['is_stock']
                    del company['pin_yin']

            if 'items' in item:
                cls._company_industry_tree_items(item['items'])

    @classmethod
    def _max(cls, items):
        max = None
        for item in items:
            if is_invalid_target_val(item):
                continue
            if max is None or max < item:
                max = item
        return max

    @classmethod
    def _min(cls, items):
        min = None
        for item in items:
            if is_invalid_target_val(item):
                continue
            if min is None or min > item:
                min = item
        return min

    @classmethod
    def normal_values(cls, items):
        max0 = cls._max(items)
        min0 = cls._min(items)
        if max0 is None or min0 is None:
            return items
        if abs(max0) <= 1 and abs(min0) <= 1:
            return items
        max0 = abs(max0)
        if max0 < abs(min0):
            max0 = abs(min0)
        return cls._rebuild_normal_items(items, max0)

    @classmethod
    def _rebuild_normal_items(cls, items, max_value):
        result = list()
        for item in items:
            if item == is_invalid_target_val(item):
                result.append(item)
            else:
                result.append(format_float(item * 1.0 / max_value))
        return result

    @classmethod
    def get_user_view_config(cls, uid, view_type):
        return UserViewConfig.find_config(uid, view_type)

    @classmethod
    def save_user_view_config(cls, uid, view_type, config, company_code=''):
        if not company_code:
            company_code = config.get('company_code') or ''
        config.pop('uid', None)
        config.pop('company_code', None)
        UserViewConfig.save_config(uid, view_type, config, company_code)
        return config

    @classmethod
    def get_company_model_class(cls, company_code, industry_id=None, default_value=None):
        if not company_code:
            return COMMON_MODEL_CLASS
        model_class = ComapnyModelClassManager().get_model_class(company_code)
        if not model_class:
            return default_value
        return model_class

    @classmethod
    def get_self_target_config_params(cls, params, view_type):
        default_config = UserViewConfig.default_config(view_type)
        params['default_config'] = default_config
        targets = params.get('targets')
        targets = list(OrderedDict.fromkeys(targets))
        if targets:
            return params
        config = UserViewConfig.find_config(params['uid'], view_type)
        if not config:
            return params
        for k, v in config.items():
            if k == 'company_code' or k == 'industry_id' or k == 'industry_range':
                continue
            params[k] = config[k]
        return params

    @classmethod
    def get_target_items(cls, company_code=None, target_names=None, model_class=None):
        if not target_names:
            return list()
        if not model_class:
            model_class = ComapnyModelClassManager().get_model_class(company_code)
        if not model_class:
            sd.log_info("not found model_class for {0}".format(company_code))
            return list()
        return TargetDAO().find_targets_by_names(target_names,model_class)