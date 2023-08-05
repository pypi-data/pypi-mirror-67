from .constant_base import get_items_type_name, get_target_value_type0

TARGET_LOST_DEFAULT = 0
TARGET_LOST_ZERO = 1
TARGET_LOST_NONE = 2

TARGET_VALUE_CONVERT_NO = 0
TARGET_VALUE_CONVERT_ABS = 1
TARGET_VALUE_CONVERT_NEGTIVE_ZERO = 2
TARGET_VALUE_CONVERT_SQRT = 3

CONVERT_NAME_ABS = "abs"
CONVERT_NAME_NEGTIVE_ZERO = "zero"
CONVERT_NAME_SQRT = "sqrt"

TARGET_BODY_COMPANY = 1  # 公司
TARGET_BODY_INDUSTRY_MEAN = 2  # 行业均值
TARGET_BODY_INDUSTRY_MIDDLE = 3  # 行业中值
TARGET_BODY_INDUSTRY_REVENUE_MEAN = 4  # 行业收入加权中值
TARGET_BODY_INDUSTRY_PROFIT_MEAN = 5  # 行业利润加权中值
TARGET_BODY_INDUSTRY_ASSET_MEAN = 6  # 行业总资产加权中值

TARGET_BODY_FIRST_INDUSTRY_MEAN = 11  # 一级行业均值
TARGET_BODY_FIRST_INDUSTRY_MIDDLE = 12  # 二级行业中值
TARGET_BODY_FIRST_INDUSTRY_REVENUE_MEAN = 13  # 行业收入加权中值
TARGET_BODY_FIRST_INDUSTRY_PROFIT_MEAN = 14  # 行业利润加权中值
TARGET_BODY_FIRST_INDUSTRY_ASSET_MEAN = 15  # 行业总资产加权中值

TARGET_BODY_SECOND_INDUSTRY_MEAN = 16  # 二级行业均值
TARGET_BODY_SECOND_INDUSTRY_MIDDLE = 17  # 二级行业中值
TARGET_BODY_SECOND_INDUSTRY_REVENUE_MEAN = 18  # 行业收入加权中值
TARGET_BODY_SECOND_INDUSTRY_PROFIT_MEAN = 19  # 行业利润加权中值
TARGET_BODY_SECOND_INDUSTRY_ASSET_MEAN = 20  # 行业总资产加权中值


def get_industry_target_type(target_body):
    if target_body == TARGET_BODY_INDUSTRY_MEAN or target_body == TARGET_BODY_FIRST_INDUSTRY_MEAN or target_body == TARGET_BODY_SECOND_INDUSTRY_MEAN:
        return TARGET_BODY_INDUSTRY_MEAN
    if target_body == TARGET_BODY_INDUSTRY_MIDDLE or target_body == TARGET_BODY_FIRST_INDUSTRY_MIDDLE or target_body == TARGET_BODY_SECOND_INDUSTRY_MIDDLE:
        return TARGET_BODY_INDUSTRY_MIDDLE
    if target_body == TARGET_BODY_INDUSTRY_REVENUE_MEAN or target_body == TARGET_BODY_FIRST_INDUSTRY_REVENUE_MEAN or target_body == TARGET_BODY_SECOND_INDUSTRY_REVENUE_MEAN:
        return TARGET_BODY_INDUSTRY_REVENUE_MEAN
    if target_body == TARGET_BODY_INDUSTRY_PROFIT_MEAN or target_body == TARGET_BODY_FIRST_INDUSTRY_PROFIT_MEAN or target_body == TARGET_BODY_SECOND_INDUSTRY_PROFIT_MEAN:
        return TARGET_BODY_INDUSTRY_PROFIT_MEAN
    if target_body == TARGET_BODY_INDUSTRY_ASSET_MEAN or target_body == TARGET_BODY_FIRST_INDUSTRY_ASSET_MEAN or target_body == TARGET_BODY_SECOND_INDUSTRY_ASSET_MEAN:
        return TARGET_BODY_INDUSTRY_ASSET_MEAN
    return None


def is_first_industry_target_type(target_body):
    return target_body >= TARGET_BODY_FIRST_INDUSTRY_MEAN and target_body <= TARGET_BODY_FIRST_INDUSTRY_ASSET_MEAN


TARGET_BODY_NAME_COMPANY = "公司指标"
TARGET_BODY_NAME_INDUSTRY_MEAN = "行业均值"
TARGET_BODY_NAME_INDUSTRY_MIDDLE = "行业中值"
TARGET_BODY_NAME_INDUSTRY_REVENUE_MEAN = "行业营收加权均值"
TARGET_BODY_NAME_INDUSTRY_PROFIT_MEAN = "行业利润加权均值"
TARGET_BODY_NAME_INDUSTRY_ASSET_MEAN = "行业资产加权均值"

TARGET_BODY_NAME_FIRST_INDUSTRY_MEAN = "行业一级算数均值"
TARGET_BODY_NAME_FIRST_INDUSTRY_MIDDLE = "行业二级算数中值"
TARGET_BODY_NAME_FIRST_INDUSTRY_REVENUE_MEAN = "行业一级营收加权均值"
TARGET_BODY_NAME_FIRST_INDUSTRY_PROFIT_MEAN = "行业一级利润加权均值"
TARGET_BODY_NAME_FIRST_INDUSTRY_ASSET_MEAN = "行业一级总资产加权均值"
TARGET_BODY_NAME_SECOND_INDUSTRY_MEAN = "行业二级算数均值"
TARGET_BODY_NAME_SECOND_INDUSTRY_MIDDLE = "行业二级算数中值"
TARGET_BODY_NAME_SECOND_INDUSTRY_REVENUE_MEAN = "行业二级营收加权均值"
TARGET_BODY_NAME_SECOND_INDUSTRY_PROFIT_MEAN = "行业二级利润加权均值"
TARGET_BODY_NAME_SECOND_INDUSTRY_ASSET_MEAN = "行业二级总资产加权均值"  # 行业总资产加权中值

TARGET_CUSTOM_BODY = [{'name': TARGET_BODY_NAME_COMPANY, 'value': TARGET_BODY_COMPANY},
                      {'name': TARGET_BODY_NAME_FIRST_INDUSTRY_MEAN, 'value': TARGET_BODY_FIRST_INDUSTRY_MEAN},
                      {'name': TARGET_BODY_NAME_SECOND_INDUSTRY_MEAN, 'value': TARGET_BODY_SECOND_INDUSTRY_MEAN},
                      {'name': TARGET_BODY_NAME_FIRST_INDUSTRY_REVENUE_MEAN,
                       'value': TARGET_BODY_FIRST_INDUSTRY_REVENUE_MEAN},
                      {'name': TARGET_BODY_NAME_SECOND_INDUSTRY_REVENUE_MEAN,
                       'value': TARGET_BODY_SECOND_INDUSTRY_REVENUE_MEAN},
                      {'name': TARGET_BODY_NAME_FIRST_INDUSTRY_PROFIT_MEAN,
                       'value': TARGET_BODY_FIRST_INDUSTRY_PROFIT_MEAN},
                      {'name': TARGET_BODY_NAME_SECOND_INDUSTRY_PROFIT_MEAN,
                       'value': TARGET_BODY_SECOND_INDUSTRY_PROFIT_MEAN},
                      {'name': TARGET_BODY_NAME_FIRST_INDUSTRY_ASSET_MEAN,
                       'value': TARGET_BODY_FIRST_INDUSTRY_ASSET_MEAN},
                      {'name': TARGET_BODY_NAME_SECOND_INDUSTRY_ASSET_MEAN,
                       'value': TARGET_BODY_SECOND_INDUSTRY_ASSET_MEAN},
                      ]
TARGET_VALUE_NUMBER = 1  # 数值
TARGET_VALUE_LAST_YEAR_RATIO = 2  # 上年同比
TARGET_VALUE_THREE_YEAR_RATIO = 3  # 3年同比
TARGET_VALUE_LAST_SEASON = 4  # 上季度环比
TARGET_VALUE_LAST_SEASON_NUMBER = 5  # 上一季度
TARGET_VALUE_LAST_YEAR_NUMBER = 6  # 上一年
TARGET_VALUE_LAST_TWO_SEASON_NUMBER = 7  # 上两季度
TARGET_VALUE_LAST_TWO_YEAR_NUMBER = 8  # 上两年
TARGET_VALUE_LAST_THREE_SEASON_NUMBER = 9  # 上三季度
TARGET_VALUE_LAST_THREE_YEAR_NUMBER = 10  # 上三年
TARGET_VALUE_LAST_FOUR_SEASON_NUMBER = 11  # 上四季度
TARGET_VALUE_LAST_FOUR_YEAR_NUMBER = 12  # 上四年
TARGET_VALUE_LAST_PERIOD_NUMBER = 13  # 上一期
TARGET_VALUE_LAST_TWO_PERIOD_NUMBER = 14  # 上两期
TARGET_VALUE_LAST_THREE_PERIOD_NUMBER = 15  # 上三期
TARGET_VALUE_LAST_FOUR_PERIOD_NUMBER = 16  # 上四期

TARGET_OPERATOR_ADD = "+"
TARGET_OPERATOR_MINUS = "-"
TARGET_OPERATOR_MULTIPLY = "*"
TARGET_OPERATOR_DIVIDE = "/"


def get_target_lost_type_name(type):
    if type == TARGET_LOST_NONE:
        return 'none'
    if type == TARGET_LOST_ZERO:
        return '0'
    return ''


def convert_target_convert_type(name):
    if name == CONVERT_NAME_ABS:
        return TARGET_VALUE_CONVERT_ABS
    if name == CONVERT_NAME_NEGTIVE_ZERO:
        return TARGET_VALUE_CONVERT_NEGTIVE_ZERO
    if name == CONVERT_NAME_SQRT:
        return TARGET_VALUE_CONVERT_SQRT
    return TARGET_VALUE_CONVERT_NO


def target_convert_type_name(type):
    if type == TARGET_VALUE_CONVERT_ABS:
        return CONVERT_NAME_ABS
    if type == TARGET_VALUE_CONVERT_NEGTIVE_ZERO:
        return CONVERT_NAME_NEGTIVE_ZERO
    if type == TARGET_VALUE_CONVERT_SQRT:
        return CONVERT_NAME_SQRT
    return ""


def convert_target_lost_type(name):
    return TARGET_LOST_DEFAULT


TARGET_CUSTOM_BODY2 = [{'name': '公司', 'value': TARGET_BODY_COMPANY},
                       {'name': '行业均值', 'value': TARGET_BODY_INDUSTRY_MEAN},
                       {'name': '行业中值', 'value': TARGET_BODY_INDUSTRY_MIDDLE},
                       {'name': '行业营收均值', 'value': TARGET_BODY_INDUSTRY_REVENUE_MEAN},
                       {'name': '行业利润均值', 'value': TARGET_BODY_INDUSTRY_PROFIT_MEAN},
                       {'name': '行业资产均值', 'value': TARGET_BODY_INDUSTRY_ASSET_MEAN}
                       ]

TARGET_CUSTOM_VALUE = [{'name': '当期数值', 'value': TARGET_VALUE_NUMBER},
                       {'name': '上期数值', 'value': TARGET_VALUE_LAST_SEASON_NUMBER},
                       {'name': '上年数值', 'value': TARGET_VALUE_LAST_YEAR_NUMBER},
                       {'name': '上年同比', 'value': TARGET_VALUE_LAST_YEAR_RATIO},
                       {'name': '三年同比', 'value': TARGET_VALUE_THREE_YEAR_RATIO},
                       {'name': '上期环比', 'value': TARGET_VALUE_LAST_SEASON}]

TARGET_CUSTOM_VALUE2 = TARGET_CUSTOM_VALUE + [
    {'name': '上两期数值', 'value': TARGET_VALUE_LAST_TWO_SEASON_NUMBER},
    {'name': '上三期数值', 'value': TARGET_VALUE_LAST_THREE_SEASON_NUMBER},
    {'name': '上四期数值', 'value': TARGET_VALUE_LAST_FOUR_SEASON_NUMBER},
]

TARGET_CUSTOM_OPERATOR = [{'name': '加', 'value': TARGET_OPERATOR_ADD},
                          {'name': '减', 'value': TARGET_OPERATOR_MINUS},
                          {'name': '乘', 'value': TARGET_OPERATOR_MULTIPLY},
                          {'name': '除', 'value': TARGET_OPERATOR_DIVIDE}]

TARGET_CUSTOM_OPERATOR2 = [{'name': '+', 'value': TARGET_OPERATOR_ADD},
                           {'name': '-', 'value': TARGET_OPERATOR_MINUS},
                           {'name': '*', 'value': TARGET_OPERATOR_MULTIPLY},
                           {'name': '%', 'value': TARGET_OPERATOR_DIVIDE}]


def is_target_operator(c):
    return c == TARGET_OPERATOR_ADD or c == TARGET_OPERATOR_MINUS or c == TARGET_OPERATOR_MULTIPLY or c == TARGET_OPERATOR_DIVIDE


def is_target_convert_word(word):
    return word == CONVERT_NAME_ABS or word == CONVERT_NAME_SQRT or word == CONVERT_NAME_NEGTIVE_ZERO


def get_target_value_type_name(value):
    return get_items_type_name(value, TARGET_CUSTOM_VALUE2)


def get_target_value_body_name(value):
    return get_items_type_name(value, TARGET_CUSTOM_BODY2)


def get_target_body_type(name):
    if name == '公司':
        return TARGET_BODY_COMPANY
    result = get_target_value_type0(name, TARGET_CUSTOM_BODY)
    if not result and name.find('行业') == 0:
        if len(name) == 4:
            name = "行业二级 " + name[2:4] + "算数均值"
        else:
            name = "行业二级" + name[2:4] + "加权均值"
        result = get_target_value_type0(name, TARGET_CUSTOM_BODY)
    return result


def get_target_value_type(name):
    value_type = get_target_value_type0(name, TARGET_CUSTOM_VALUE2)
    return value_type
