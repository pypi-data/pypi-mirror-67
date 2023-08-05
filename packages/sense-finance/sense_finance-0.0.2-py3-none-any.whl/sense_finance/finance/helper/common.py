import sense_core as sd
from sense_finance.finance.util import *
from sense_finance.finance.common import *
from sense_finance.finance.model import *
import datetime



def is_valid_operator(operator):
    return operator == TARGET_OPERATOR_ADD or operator == TARGET_OPERATOR_MINUS or operator == TARGET_OPERATOR_MULTIPLY or operator == TARGET_OPERATOR_DIVIDE


def _refine_value(value, operator):
    if value is not None:
        return value
    if operator == TARGET_OPERATOR_ADD or operator == TARGET_OPERATOR_MINUS:
        return 0
    return None


def is_monit_industry_field(str):
    return str.find('i:') == 0


def is_monit_company_field(str):
    return str.find('c:') == 0


def compute_operator_value(operator, v1, v2):
    if v1 is None and v2 is None:
        return None
    v1 = _refine_value(v1, operator)
    v2 = _refine_value(v2, operator)
    if v1 is None or v2 is None:
        return None
    if operator == TARGET_OPERATOR_ADD:
        return v1 + v2
    if operator == TARGET_OPERATOR_MINUS:
        return v1 - v2
    if operator == TARGET_OPERATOR_MULTIPLY:
        return v1 * v2
    if operator == TARGET_OPERATOR_DIVIDE:
        if v2 == 0:
            return None
        return format_float(v1 * 1.0 / v2, KEEP_NUMBER_SIZE)
    return None


def get_weight_row_names(compare_type):
    if compare_type == COMPARE_MEAN_PROFIT_WEIGHT:
        return ['利润总额']
    if compare_type == COMPARE_MEAN_REVENUE_WEIGHT:
        return ['营业收入']
    if compare_type == COMPARE_MEAN_ASSET_WEIGHT:
        return ['资产总计']
    return None


def get_last_time_interval(time_cycle_type, year, report_time_type, diff):
    if time_cycle_type == REPORT_CYCLE_YEAR:
        return year - diff, report_time_type
    while diff > 0:
        diff -= 1
        year, report_time_type = _get_season_last_time_interval(time_cycle_type, year, report_time_type)
    return year, report_time_type


def _get_season_last_time_interval(time_cycle_type, year, report_time_type):
    report_time_types = get_report_time_types(time_cycle_type)
    index = report_time_types.index(report_time_type)
    if index == len(report_time_types) - 1:
        return year - 1, report_time_types[0]
    return year, report_time_types[index + 1]


def compute_target_ratio(val, vals):
    val2 = sum(vals) * 1.0 / len(vals)
    if val2 == 0:
        return None
    return format_float((val - val2) * 1.0 / val2, KEEP_NUMBER_SIZE)


def compute_simple_mean(field, items):
    if len(items) == 0:
        return None
    total = 0
    size = 0
    for item in items:
        val = item.get_attr(field)
        if val is None:
            continue
        size += 1
        total += val
    if size == 0:
        return None
    return total / size


def get_lastest_time_range_type(report_time_type):
    if report_time_type == REPORT_CYCLE_YEAR:
        return REPORT_TIME_RANGE_TWO
    month = datetime.datetime.now().month
    if month >= 6:
        return REPORT_TIME_RANGE_CURRENT
    return REPORT_TIME_RANGE_ONE
