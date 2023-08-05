from sense_finance.finance.common import *
from .base import BaseTargetComputer
from sense_finance.finance.helper import *


class CompanyTargetComputer(BaseTargetComputer):
    """
        计算公司和同行业指标数据，返回的结构：
        {
            "target_header":[
            {
                name:"营业收入",
                desc:"xxxx",
                self:"母公司",
                mean:"算数平均"
            }
            ],
            "target_items":[
            {
                "time":"2017",
                "items":[
                {
                    "self":"20",
                    "mean":"10"
                }
                ]
            }
            ]
        }
    """

    def compute(self, condition):
        result = dict()
        result['target_header'] = self.build_target_header(condition)
        result['target_items'] = self._compute_target_items(condition)
        return result

    def _compute_target_items(self, condition):
        if condition.report_time_type == REPORT_CYCLE_YEAR:
            condition.select_start_year -= 1
        target_container = self.target_data_dao.select_target_result(condition)
        sd.log_info("target_container time_data_map={0}".format(target_container.time_data_map.keys()))
        self.build_report_time_items(condition, target_container)
        return self.parse_target_result(condition, target_container)

    '''
    结构 {
        周期组合key:{
            {
                'company_name':value
            }
        }
    }
    '''

    def parse_target_result(self, condition, target_container):
        result = list()
        targets = condition.targets
        industry_container = self.industry_data_dao.select_data(condition)
        for i, time_item in enumerate(self.report_select_time_items):
            year, time_type = time_item
            key = get_report_time_key(year, time_type)
            line = {
                'time': get_show_report_time(condition.report_time_type, year, time_type),
                'items': list()
            }
            if condition.ratio_type == 0:
                year1, time_type1 = self.report_select_time_items[i + 1]
            else:
                year1 = year - 1
                time_type1 = time_type
            key1 = get_report_time_key(year1, time_type1)
            for target in targets:
                self0, mean = self._get_single_time_targets(condition, key, target, target_container,
                                                            industry_container)
                self1, mean1 = self._get_single_time_targets(condition, key1, target, target_container,
                                                             industry_container)
                self_way, self_ratio = self.get_target_value_way_ratio(self0, self1)
                mean_way, mean_ratio = self.get_target_value_way_ratio(mean, mean1)
                line['items'].append({
                    'self_way': self_way,
                    'self_ratio': self_ratio,
                    'mean_way': mean_way,
                    'mean_ratio': mean_ratio,
                    'self_native': convert_target_show_value(target, self0),
                    'self': convert_target_normal_value(target, self0),
                    'mean': convert_target_normal_value(target, mean),
                })
            result.append(line)
            if i >= len(self.report_time_items) - 1:
                break
        return result

    def _get_single_time_targets(self, condition, year_time_key, target, target_container, industry_container
                                 ):
        field = target.field_key
        item = industry_container.get_item(field, year_time_key)
        if item:
            mean = item.value
        else:
            mean = None
        items = target_container.time_data_items(year_time_key)
        if not items:
            return None, mean
        self0 = self._get_self_target(condition.company_id, field, items)
        return self0, mean

    def _get_self_target(self, company_id, field, items):
        for item in items:
            if company_id == item.company_id:
                return item.get_attr(field)
        return None

    def build_target_header(self, condition):
        result = list()
        self0 = get_report_bore_name(condition.combine_type)
        mean = get_compare_mean_name(condition.compare_type)
        if condition.ratio_type == 0:
            ratio_name = "(环比变化)"
        else:
            ratio_name = "(同比变化)"
        for target in condition.targets:
            result.append({
                'id': target.id,
                'name': show_target_name(target),
                'desc': build_target_desc(target),
                'self': self0 + ratio_name,
                'mean': mean + ratio_name,
            })
        return result
