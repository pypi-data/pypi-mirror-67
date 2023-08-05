from sense_finance.finance.util import *
from sense_finance.finance.dao import *
from sense_finance.finance.model import *
from sense_finance.finance.target import CompanyTargetComputer
from sense_finance.finance.helper import *
from .base import BaseFinanceService


class CompanyTargetComputeService(BaseFinanceService):

    @classmethod
    def compute(cls, params):
        params = cls.get_self_target_config_params(params, VIEW_TYPE_COMPANY_REPORT)
        condition = cls._build_condition(params)
        result = CompanyTargetComputer().compute(condition)
        graph_result = cls._build_graph(result)
        if graph_result:
            result['graph_items'] = cls._normal_graph_items(graph_result, result)
            result['native_graph_items'] = graph_result
        else:
            result['graph_items'] = list()
            result['native_graph_items'] = list()
        return condition, result

    @classmethod
    @sd.try_catch_exception
    def _build_graph(cls, result):
        graph_result = list()
        target_header = result.get('target_header')
        if not target_header:
            sd.log_info("no header for {}".format(result))
            return graph_result
        target_items = result['target_items']
        for i, header in enumerate(target_header):
            items = list()
            for target_item in target_items:
                self0 = target_item['items'][i]['self_native']
                items.append(self0)
            graph_result.append(items)
        return graph_result

    @classmethod
    def _normal_graph_items(cls, graph_result, result):
        if not graph_result:
            return list()
        header = result['target_header']
        result = list()
        for i, items in enumerate(graph_result):
            if header[i]['name'].find('(%)') > 0:
                items = [item / 100 for item in items]
            result.append(cls.normal_values(items))
        return result

    @classmethod
    def _build_condition(cls, params):
        params['model_name'] = ""
        report_time_type = params['report_time_type']
        time_range_type = params['time_range_type']
        combine_type = params['combine_type']
        compare_type = params['compare_type']
        ratio_type = params.get('ratio_type') or 0
        company_dao = CompanyDAO()
        info = company_dao.get_company(params['company_code'])
        if not info:
            sd.log_info("_build_condition company failed for {}".format(params))
            raise Exception('公司参数无效')
        industry_range = cls.check_param_industry_range(params, info)
        targets = cls.get_target_items(params['company_code'], params['targets'])
        if not targets:
            params['targets'] = params['default_config']['targets']
            params['use_default'] = True
            targets = cls.get_target_items(params['company_code'], params['targets'])
            if not targets:
                sd.log_info("_build_condition target failed for {}".format(params))
                raise Exception('指标参数无效')
        params['model_name'] = targets[0].model_name
        condition = TargetCondition(report_time_type=report_time_type, time_range_type=time_range_type,
                                    combine_type=combine_type, compare_type=compare_type,
                                    company=info, company_list=None, industry_id=industry_range,
                                    targets=targets, user_id=params['uid'],check_year_range=True)
        condition.ratio_type = ratio_type
        return condition
