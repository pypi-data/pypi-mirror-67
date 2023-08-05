from .base import BaseTargetComputer
from sense_finance.finance.helper import *
from sense_finance.finance.common import *


class IndustryMeanComputer(BaseTargetComputer):

    def compute(self, condition, report_time_items, report_select_time_items):
        result = list()
        if not report_time_items:
            return result
        # condition.select_start_year -= 1
        industry_container = self.industry_data_dao.select_data(condition)
        target_types = condition.compare_type
        target_data_list = {type: list() for type in target_types}
        for target in condition.targets:
            target_data = {type: list() for type in target_types}
            target_native_data = {type: list() for type in target_types}
            target_new_data = {type: list() for type in target_types}
            industry_target_map = industry_container.get_map(target.field_key) or dict()
            for i, time_item in enumerate(report_select_time_items):
                year, time_type = time_item
                year2, time_type2 = report_select_time_items[i + 1]
                key = get_report_time_key(year, time_type)
                key2 = get_report_time_key(year2, time_type2)
                items = industry_target_map.get(key)
                items2 = industry_target_map.get(key2)
                if not items2:
                    item_map2 = dict()
                else:
                    item_map2 = {x.target_type: x for x in items2}
                if not items:
                    item_map = dict()
                else:
                    item_map = {x.target_type: x for x in items}

                for target_type in target_types:
                    item = item_map.get(target_type)
                    val = item.value if item is not None else INVALID_TARGET_DATA
                    item2 = item_map2.get(target_type)
                    val2 = item2.value if item2 is not None else INVALID_TARGET_DATA
                    way, ratio = self.get_target_value_way_ratio(val, val2)
                    target_native_data[target_type].append(convert_target_show_value(target, val))
                    target_data[target_type].append(convert_target_normal_value(target, val))
                    target_new_data[target_type].append({
                        'way': way,
                        'ratio': ratio,
                        'native_value': convert_target_show_value(target, val),
                        'value': convert_target_normal_value(target, val)
                    })
                if i >= len(report_time_items) - 1:
                    break

            for target_type in target_types:
                target_data_list[target_type].append(
                    {
                        'name': target.name,
                        'new_items': target_new_data[target_type],
                        'items': target_data[target_type],
                        'native_items': target_native_data[target_type]
                    }
                )

        for target_type in target_types:
            result.append(
                {
                    'name': get_industry_target_name(target_type),
                    'items': target_data_list[target_type]
                }
            )
        return result
