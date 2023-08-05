from sense_finance.finance.util import *
from sense_finance.finance.dao import *
from sense_finance.finance.model import *
from sense_finance.finance.target import IndustryCompanyTargetComputer
from .base import BaseFinanceService


class IndustryCompanyTargetService(BaseFinanceService):

    @classmethod
    def compute(cls, params):
        params = cls.get_self_target_config_params(params, VIEW_TYPE_INDUSTRY_REPORT)
        condition = cls._build_condition(params)
        sd.log_info("params={0}".format(params))
        if type(condition) == str:
            return condition, None
        result = IndustryCompanyTargetComputer().compute(condition)
        cls._format_result(result)
        return condition, result

    @classmethod
    def _rebuild_float_values(cls, items):
        return [cls._parse_target_float_value(item) for item in items]

    @classmethod
    def _parse_target_float_value(cls, val):
        if is_invalid_target_val(val):
            return val
        return parse_float(val, INVALID_TARGET_DATA)

    @classmethod
    @sd.try_catch_exception
    def _format_result(cls, result):
        target_items = result['industry_targets']
        for i, target_item in enumerate(target_items):
            for item in target_item['items']:
                items = item['native_items']
                item['values'] = cls.normal_values(cls._rebuild_float_values(items))
        target_items = result['company_targets']
        for i, target_item in enumerate(target_items):
            for item in target_item['items']:
                values = list()
                for item0 in item['items']:
                    values.append(item0['native_value'])
                item['values'] = cls.normal_values(cls._rebuild_float_values(values))

    @classmethod
    def _build_condition(cls, params):
        params['model_name'] = ""
        report_time_type = params['report_time_type']
        time_range_type = params['time_range_type']
        compare_type = params['compare_type']
        limit_type = params['limit_type']
        combine_type = params['combine_type']
        company_code = params['company_code']
        industry_id = params.get('industry_id')
        ratio_type = params.get('ratio_type') or 0
        info = None
        company_dao = CompanyDAO()
        if company_code:
            info = company_dao.get_company(params['company_code'])
            if not info:
                sd.log_info("_build_condition company failed for {}".format(params))
                return '公司参数无效'
            industry_range = cls.check_param_industry_range(params, info)
            industry_id = industry_range
        if not industry_id:
            sd.log_info("invalid industry_id={0} for params={1} info={2}".format(industry_id, params, info))
            return '行业参数无效'
        companies = company_dao.gets_by_industry_id(industry_id, params['uid'], use_model_class=True)
        sd.log_info(
            "gets_by_industry_id companies = {0} for industry_id={1} uid={2}".format(len(companies), industry_id,
                                                                                     params['uid']))
        if not companies:
            return '行业{}查询无可用公司'.format(industry_id)
        if not info and compare_type == COMPANY_COMPARE_TYPE_NEAR:
            compare_type = COMPANY_COMPARE_TYPE_TOP
            params['compare_type'] = compare_type
        code = company_code
        if not code:
            code = companies[0].company_code
        if code:
            compare_targets = cls.get_target_items(code, [params['compare_target']])
        else:
            index = 0
            compare_targets = None
            for company in companies:
                index += 1
                compare_targets = cls.get_target_items(company.company_code, [params['compare_target']])
                if not code:
                    code = company.company_code
                if index > 4 or compare_targets:
                    break
        if not compare_targets:
            sd.log_info("_build_condition compare_target not valid for {0} code={1}".format(params, code))
            params['compare_target'] = params['default_config']['compare_target']
            compare_targets = cls.get_target_items(code, [params['compare_target']])
            if not compare_targets:
                sd.log_info("_build_condition compare_target failed for {0} code={1}".format(params, code))
                return '比较指标参数无效'
            sd.log_info("use default compare_target={}".format(params['compare_target']))
        targets = cls.get_target_items(code, params['targets'])
        if not targets:
            params['targets'] = params['default_config']['targets']
            params['use_default'] = True
            targets = cls.get_target_items(code, params['targets'])
            if not targets:
                sd.log_info("_build_condition target failed for {}".format(params))
                return '指标参数无效'
        params['model_name'] = targets[0].model_name
        condition = TargetCondition(report_time_type=report_time_type, time_range_type=time_range_type,
                                    compare_type=compare_type, limit_type=limit_type,
                                    company=info, compare_target=compare_targets[0], targets=targets,
                                    company_list=companies, combine_type=combine_type, user_id=params['uid'],
                                    industry_id=industry_id, check_year_range=True)
        condition.ratio_type = ratio_type
        return condition
