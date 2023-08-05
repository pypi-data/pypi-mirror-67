from sense_finance.finance.util import *
from sense_finance.finance.dao import *
from sense_finance.finance.model import *
from .base import BaseFinanceService
from sense_finance.finance.common.redis_store import *
from .target_show import TargetShowService
from sense_finance.finance.common.constants import get_finance_radar_key


class FinanceService(BaseFinanceService):

    @classmethod
    def get_finance_select_params(cls, uid, company_code):
        _res = list()
        _res.append({'name': 'report_time_type', 'items': REPORT_CYCLE})
        _res.append({'name': 'time_range_type', 'items': REPORT_TIME_RANGE})
        _res.append({'name': 'combine_type', 'items': REPORT_BORE})
        _res.append({'name': 'compare_type', 'items': COMPARE_MEAN})
        _res.append({'name': 'ratio_type', 'items': RATIO_TYPE})
        _res.append({'name': 'industry', 'items': cls.build_company_industry_ranges(company_code)})
        _res.append({'name': 'targets', 'items': TargetShowService.company_targets_show(company_code, uid)})
        return _res

    @classmethod
    def get_industry_select_params(cls, uid, company_code, industry_id=None):
        _res = list()
        _res.append({'name': 'report_time_type', 'items': REPORT_CYCLE})
        _res.append({'name': 'time_range_type', 'items': REPORT_TIME_RANGE})
        _res.append({'name': 'limit_type', 'items': LIMIT_TYPE})
        _res.append({'name': 'ratio_type', 'items': RATIO_TYPE})
        _res.append({'name': 'combine_type', 'items': REPORT_BORE})
        _res.append({'name': 'industry', 'items': cls.build_company_industry_ranges(company_code)})
        if industry_id:
            _res.append({'name': 'company_compare_type', 'items': INDUSTRY_COMPARE_TYPE})
        else:
            _res.append({'name': 'company_compare_type', 'items': COMPANY_COMPARE_TYPE})
        _res.append(
            {'name': 'targets', 'items': TargetShowService.company_targets_show(company_code, uid, industry_id)})
        return _res

