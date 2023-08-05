from .constant_base import *

MONITOR_UNIT_BASIC = 0
MONITOR_UNIT_WAN = 1
MONITOR_UNIT_YI = 2
MONITOR_UNIT_PERCENT = 3

MONITOR_TIME_CURRENT_PERIOD = 1
MONITOR_TIME_PREVIOUS_PERIOD = 2
MONITOR_TIME_CURRENT_YEAR = 3
MONITOR_TIME_PREVIOUS_YEAR = 4
MONITOR_TIME_CURRENT_QUARTER = 5
MONITOR_TIME_PREVIOUS_QUARTER = 6

MONITOR_OPERATOR_MORE = ">"
MONITOR_OPERATOR_LESS = "<"
MONITOR_OPERATOR_MORE_OR_EQUAL = ">="
MONITOR_OPERATOR_LESS_OR_EQUAL = "<="
MONITOR_OPERATOR_EQUAL = "="
MONITOR_OPERATOR_NO_EQUAL = "!="

MONITOR_FORMULA_RELATION_AND = '且'
MONITOR_FORMULA_RELATION_OR = '或'

MONITOR_UNIT_TYPES = [
    {'name': '万', 'value': MONITOR_UNIT_WAN},
    {'name': '亿', 'value': MONITOR_UNIT_YI},
    {'name': '数值', 'value': MONITOR_UNIT_BASIC},
    {'name': '%', 'value': MONITOR_UNIT_PERCENT},
]

MONITOR_UNIT_TYPES2 = [
    {'name': '万', 'value': '万'},
    {'name': '亿', 'value': '亿'},
    {'name': '数值', 'value': ''},
    {'name': '百分比', 'value': '%'},
]

MONITOR_OPERATOR = [
    {'name': '>', 'value': MONITOR_OPERATOR_MORE},
    {'name': '<', 'value': MONITOR_OPERATOR_LESS},
    {'name': '≥', 'value': MONITOR_OPERATOR_MORE_OR_EQUAL},
    {'name': '≤', 'value': MONITOR_OPERATOR_LESS_OR_EQUAL},
    {'name': '=', 'value': MONITOR_OPERATOR_EQUAL},
    {'name': '≠', 'value': MONITOR_OPERATOR_NO_EQUAL},
]

MONITOR_TIME_TYPE = [{'name': '最近报告期', 'value': MONITOR_TIME_CURRENT_PERIOD},
                     {'name': '上一报告期', 'value': MONITOR_TIME_PREVIOUS_PERIOD},
                     {'name': '最近年度', 'value': MONITOR_TIME_CURRENT_YEAR},
                     {'name': '上一年度', 'value': MONITOR_TIME_PREVIOUS_YEAR},
                     {'name': '最近季度', 'value': MONITOR_TIME_CURRENT_QUARTER},
                     {'name': '上一季度', 'value': MONITOR_TIME_PREVIOUS_QUARTER}]

MONITOR_FORMULA_RELATION = [{'name': MONITOR_FORMULA_RELATION_AND, 'value': 'and'},
                            {'name': MONITOR_FORMULA_RELATION_OR, 'value': 'or'}]


def is_monit_relation_operator(c):
    return c == MONITOR_FORMULA_RELATION_OR or c == MONITOR_FORMULA_RELATION_AND


def is_monit_compare_operator(c):
    return get_target_value_type0(c, MONITOR_OPERATOR) is not None


def get_monitor_relation_type_name(value):
    return get_items_type_name(value, MONITOR_FORMULA_RELATION)


def get_monitor_unit_type_name(value):
    return get_items_type_name(value, MONITOR_UNIT_TYPES)


def get_monitor_unit_type(name):
    return get_target_value_type0(name, MONITOR_UNIT_TYPES)


def get_monitor_operator_type_name(value):
    return get_items_type_name(value, MONITOR_OPERATOR)

def get_monitor_operator_type(name):
    return get_target_value_type0(name, MONITOR_OPERATOR)

def get_monit_time_type_name(value):
    return get_items_type_name(value, MONITOR_TIME_TYPE)


def get_monit_time_type(name):
    return get_target_value_type0(name, MONITOR_TIME_TYPE)
