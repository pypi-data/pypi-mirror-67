from .base import BaseTargetComputer
from sense_finance.finance.helper import *


class IndustryCandidateComputer2(BaseTargetComputer):

    def compute(self, condition):
        industry_level = get_industry_level(condition.industry_id)
        if industry_level is None:
            sd.log_info("compute candidate industry_id invalid for {}".format(condition.industry_id))
            return list()
        items0 = self.report_data_dao.find_industry_latest_target_data(industry_level, condition.industry_id,
                                                                       condition.combine_type,
                                                                       condition.report_time_type,
                                                                       condition.compare_target.id)
        items = list()
        for item in items0:
            items.append({
                'company_id': item.company_code,
                'target': item.value,
                'rank': 0
            })
        items = sorted(items, key=lambda x: x['target'])
        for i, item in enumerate(items):
            item['rank'] = len(items) - i
        company_item = self._get_company_item(condition, items)
        sd.log_info("_get_compare_limit_company_list={0} company_item={1}".format(len(items), company_item))
        if condition.compare_type == COMPANY_COMPARE_TYPE_NEAR:
            val = company_item['target'] if company_item else 0
            items = sorted(items, key=lambda x: abs(x['target'] - val))
        elif condition.compare_type == COMPANY_COMPARE_TYPE_TOP:
            items.reverse()
        if condition.limit_type == LIMIT_TYPE_TOP5:
            if len(items) > 5:
                items = items[0:5]
        elif condition.limit_type == LIMIT_TYPE_TOP10:
            if len(items) > 10:
                items = items[0:10]
        elif condition.limit_type == LIMIT_TYPE_TOP3:
            if len(items) > 3:
                items = items[0:3]
        if condition.compare_type == COMPANY_COMPARE_TYPE_NEAR:
            items = sorted(items, key=lambda x: x['rank'])
        if not company_item and condition.company_id:
            company_item = {
                'company_id': condition.company_id,
                'target': None,
                'rank': 0
            }
        if company_item:
            if company_item in items:
                items.remove(company_item)
            items.insert(0, company_item)
        return items

    def _get_company_item(self, condition, items):
        if not condition.company_id:
            return None
        index = -1
        company_item = None
        for i, item in enumerate(items):
            if condition.company_id == item['company_id']:
                index = i
                company_item = item
                break
        if index == -1:
            sd.log_error("not found company_target for {0} with {1}".format(condition.company_id, items))
            return None
        return company_item
