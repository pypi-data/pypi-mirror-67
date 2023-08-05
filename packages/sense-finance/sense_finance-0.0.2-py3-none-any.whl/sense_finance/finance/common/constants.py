from .constant_custom_target import *
from .constant_custom_monit import *

REPORT_BORE_COMBINE = 1
REPORT_BORE_PARENT = 2

REPORT_TIME_TYPE_FIRST_QUARTER = 1
REPORT_TIME_TYPE_HALF_YEAR = 2
REPORT_TIME_TYPE_THREE_QUARTER = 3
REPORT_TIME_TYPE_YEAR = 4

REPORT_TIME_TYPE_ONE_TO_THREE = 0
REPORT_TIME_TYPE_FOUR_TO_SIX = 5
REPORT_TIME_TYPE_SEVEN_TO_NINE = 6
REPORT_TIME_TYPE_TEN_TO_TWELVE = 7

REPORT_TYPE_BALANCE_SHEET = 3
REPORT_TYPE_CASH_FLOW = 2
REPORT_TYPE_PROFIT = 1

REPORT_CYCLE_YEAR = 1
REPORT_CYCLE_PERIOD = 2
REPORT_CYCLE_QUARTER = 3

REPORT_TIME_RANGE_THREE = 1
REPORT_TIME_RANGE_FIVE = 2
REPORT_TIME_RANGE_CURRENT = 3
REPORT_TIME_RANGE_ONE = 4
REPORT_TIME_RANGE_TWO = 5
REPORT_TIME_RANGE_SIX = 6

COMPARE_MEAN_SIMPLE = 1
COMPARE_MEAN_REVENUE_WEIGHT = 2
COMPARE_MEAN_PROFIT_WEIGHT = 3
COMPARE_MEAN_ASSET_WEIGHT = 4

INDUSTRY_TARGET_MEAN = 5
INDUSTRY_TARGET_MAX = 6
INDUSTRY_TARGET_MIDDLE = 7
INDUSTRY_TARGET_MIN = 8

COMPANY_COMPARE_TYPE_NEAR = 1  # 相邻
COMPANY_COMPARE_TYPE_TOP = 2  # 最高
COMPANY_COMPARE_TYPE_LOW = 3  # 最低

LIMIT_TYPE_TOP3 = 0
LIMIT_TYPE_TOP5 = 1
LIMIT_TYPE_TOP10 = 2

INVALID_TARGET_DATA = '-'
COMPUTING_TARGET_DATA = '计算中'

FINANCE_TARGET_ITEM_PROFIT = 1
FINANCE_TARGET_ITEM_CASH_FLOW = 2
FINANCE_TARGET_ITEM_BALANCE_SHEET = 3
FINANCE_TARGET_ITEM_STATISTICS = 4
FINANCE_TARGET_ITEM_CUSTOM = 5

TARGET_STATUS_PRIVATE = 0
TARGET_STATUS_PUBLIC = 1

TARGET_USE = 1
TARGET_NO_USE = 0

CUSTOM_TARGET_CONCURRENT_NUM = 3

MONITOR_TYPE_FINANCE = 1
MONITOR_TYPE_RISK = 2
MONITOR_TYPE_CUSTOM = 3

VIEW_TYPE_COMPANY_REPORT = 1
VIEW_TYPE_INDUSTRY_REPORT = 2
VIEW_TYPE_COMPANY_GAMBLE = 3

COMPANY_RISK_STATUS_BAD = 0
COMPANY_RISK_STATUS_NOMAL = 1
COMPANY_RISK_STATUS_GOOD = 2

COMPANY_RISK_LEVEL_HIGH = 1
COMPANY_RISK_LEVEL_LOW = 0

COMPANY_TYPE_SENSEDEAL = 1
COMPANY_TYPE_ZHAOHANG = 2
COMPANY_TYPE_CUSTOM = 3

ROW_DIM_YUAN = 1
ROW_DIM_PERCENT = 2
ROW_DIM_NO = 3
ROW_DIM_DAY = 4
ROW_DIM_TIMES = 5

WAY_UP = 1
WAY_DOWN = -1
WAY_NO = 0

INDUSTRY_LEVEL_ONE = 1
INDUSTRY_LEVEL_TWO = 2
INDUSTRY_LEVEL_THREE = 3
INDUSTRY_LEVEL_FOUR = 4

MONIT_RANGE_INDUSTRY = 1
MONIT_RANGE_COMPANY = 2

KEEP_NUMBER_SIZE = 6

MONIT_TYPE_NORMAL = 0
MONIT_TYPE_IGNORE = 1

MONIT_MESSAGE_ALL = 0
MONIT_MESSAGE_SELF = 1
MONIT_MESSAGE_SPREAD = 2
MONIT_MESSAGE_IGNORE = 3

COMMON_MODEL_CLASS = '010'
BANK_MODEL_CLASS = "070"
BOND_MODEL_CLASS = "130"
INSURE_MODEL_CLASS = "190"

MODEL_CLASS_ITEMS = [COMMON_MODEL_CLASS, BANK_MODEL_CLASS, BOND_MODEL_CLASS, INSURE_MODEL_CLASS]

ROW_DIM_TYPES = [
    {'name': '万元', 'value': ROW_DIM_YUAN},
    {'name': '百分比', 'value': ROW_DIM_PERCENT},
    {'name': '天数', 'value': ROW_DIM_DAY},
    {'name': '次数', 'value': ROW_DIM_TIMES},
    {'name': '数值', 'value': ROW_DIM_NO},
]

INDUSTRY_TARGET_TYPES = [
    COMPARE_MEAN_SIMPLE,
    COMPARE_MEAN_REVENUE_WEIGHT,
    COMPARE_MEAN_PROFIT_WEIGHT,
    COMPARE_MEAN_ASSET_WEIGHT,
    INDUSTRY_TARGET_MEAN,
    INDUSTRY_TARGET_MAX,
    INDUSTRY_TARGET_MIDDLE,
    INDUSTRY_TARGET_MIN
]


def get_weight_types():
    return [COMPARE_MEAN_REVENUE_WEIGHT, COMPARE_MEAN_PROFIT_WEIGHT, COMPARE_MEAN_ASSET_WEIGHT]


def get_company_type(company_code):
    return COMPANY_TYPE_SENSEDEAL


def is_current_stage_monit_time(time):
    return time == MONITOR_TIME_CURRENT_PERIOD or time == MONITOR_TIME_CURRENT_YEAR or time == MONITOR_TIME_CURRENT_QUARTER


def is_compare_weight_mean(target_type):
    return target_type == COMPARE_MEAN_REVENUE_WEIGHT or target_type == COMPARE_MEAN_PROFIT_WEIGHT or target_type == COMPARE_MEAN_ASSET_WEIGHT


def is_number_target_value(type):
    return type == TARGET_VALUE_LAST_YEAR_NUMBER or type == TARGET_VALUE_LAST_SEASON_NUMBER \
           or type == TARGET_VALUE_NUMBER or type == TARGET_VALUE_LAST_TWO_SEASON_NUMBER \
           or type == TARGET_VALUE_LAST_TWO_YEAR_NUMBER or type == TARGET_VALUE_LAST_THREE_SEASON_NUMBER \
           or type == TARGET_VALUE_LAST_THREE_YEAR_NUMBER or type == TARGET_VALUE_LAST_FOUR_SEASON_NUMBER \
           or type == TARGET_VALUE_LAST_FOUR_YEAR_NUMBER or type == TARGET_VALUE_LAST_PERIOD_NUMBER \
           or type == TARGET_VALUE_LAST_TWO_PERIOD_NUMBER or type == TARGET_VALUE_LAST_THREE_PERIOD_NUMBER \
           or type == TARGET_VALUE_LAST_FOUR_PERIOD_NUMBER


def is_last_season_target_value(type):
    return type == TARGET_VALUE_LAST_SEASON or type == TARGET_VALUE_LAST_SEASON_NUMBER


def get_last_season_target_value_diff(type):
    if type == TARGET_VALUE_LAST_SEASON or type == TARGET_VALUE_LAST_SEASON_NUMBER:
        return 1
    if type == TARGET_VALUE_LAST_TWO_SEASON_NUMBER:
        return 2
    if type == TARGET_VALUE_LAST_THREE_SEASON_NUMBER:
        return 3
    if type == TARGET_VALUE_LAST_FOUR_SEASON_NUMBER:
        return 4
    return 0


def get_last_period_target_value_diff(type):
    if type == TARGET_VALUE_LAST_PERIOD_NUMBER:
        return 1
    if type == TARGET_VALUE_LAST_TWO_PERIOD_NUMBER:
        return 2
    if type == TARGET_VALUE_LAST_THREE_PERIOD_NUMBER:
        return 3
    if type == TARGET_VALUE_LAST_FOUR_PERIOD_NUMBER:
        return 4
    return 0


def get_last_year_target_value_diff(type):
    if type == TARGET_VALUE_LAST_YEAR_RATIO or type == TARGET_VALUE_LAST_YEAR_NUMBER:
        return 1
    if type == TARGET_VALUE_LAST_TWO_YEAR_NUMBER:
        return 2
    if type == TARGET_VALUE_LAST_THREE_YEAR_NUMBER or type == TARGET_VALUE_THREE_YEAR_RATIO:
        return 3
    if type == TARGET_VALUE_LAST_FOUR_YEAR_NUMBER:
        return 4
    return 0


def is_last_year_target_value(type):
    return type == TARGET_VALUE_LAST_YEAR_RATIO or type == TARGET_VALUE_LAST_YEAR_NUMBER


def get_monit_time_diff(type):
    if type is not None:
        type = int(type)
    if type == MONITOR_TIME_PREVIOUS_YEAR:
        return 2
    return 1


def get_target_value_diff(type):
    if type is not None:
        type = int(type)
    if type == TARGET_VALUE_LAST_FOUR_YEAR_NUMBER:
        return 4
    if type == TARGET_VALUE_LAST_TWO_YEAR_NUMBER:
        return 2
    if type == TARGET_VALUE_THREE_YEAR_RATIO or type == TARGET_VALUE_LAST_THREE_YEAR_NUMBER:
        return 3
    if type == TARGET_VALUE_NUMBER:
        return 0
    return 1


def get_monit_report_time_type(monit_time):
    if monit_time is not None:
        monit_time = int(monit_time)
    if monit_time == MONITOR_TIME_CURRENT_PERIOD or monit_time == MONITOR_TIME_PREVIOUS_PERIOD:
        return REPORT_CYCLE_PERIOD
    if monit_time == MONITOR_TIME_CURRENT_YEAR or monit_time == MONITOR_TIME_PREVIOUS_YEAR:
        return REPORT_CYCLE_YEAR
    if monit_time == MONITOR_TIME_PREVIOUS_QUARTER or monit_time == MONITOR_TIME_CURRENT_QUARTER:
        return REPORT_CYCLE_QUARTER
    return None


def get_industry_target_name(type):
    if type == INDUSTRY_TARGET_MEAN or type == COMPARE_MEAN_SIMPLE:
        return '行业均值'
    if type == INDUSTRY_TARGET_MAX:
        return '行业最大值'
    if type == INDUSTRY_TARGET_MIDDLE:
        return '行业中值'
    if type == INDUSTRY_TARGET_MIN:
        return '行业最小值'
    return None


def get_report_month(period):
    if period == REPORT_TIME_TYPE_FIRST_QUARTER or period == REPORT_TIME_TYPE_ONE_TO_THREE:
        return 3
    elif period == REPORT_TIME_TYPE_HALF_YEAR or period == REPORT_TIME_TYPE_FOUR_TO_SIX:
        return 6
    elif period == REPORT_TIME_TYPE_THREE_QUARTER or period == REPORT_TIME_TYPE_SEVEN_TO_NINE:
        return 9
    elif period == REPORT_TIME_TYPE_YEAR or period == REPORT_TIME_TYPE_TEN_TO_TWELVE:
        return 12
    return None


def get_limit_type_value(type):
    if type == LIMIT_TYPE_TOP5:
        return 5
    if type == LIMIT_TYPE_TOP3:
        return 3
    return 10


def is_percent_target_value_type(type):
    return type == TARGET_VALUE_LAST_YEAR_RATIO or type == TARGET_VALUE_LAST_SEASON or type == TARGET_VALUE_THREE_YEAR_RATIO


REPORT_CYCLE_QUARTERS = [REPORT_TIME_TYPE_TEN_TO_TWELVE, REPORT_TIME_TYPE_SEVEN_TO_NINE, REPORT_TIME_TYPE_FOUR_TO_SIX,
                         REPORT_TIME_TYPE_ONE_TO_THREE]

REPORT_CYCLE_PERIODS = [REPORT_TIME_TYPE_YEAR, REPORT_TIME_TYPE_THREE_QUARTER, REPORT_TIME_TYPE_HALF_YEAR,
                        REPORT_TIME_TYPE_FIRST_QUARTER]


def get_possible_report_cycle_types(type):
    if type == REPORT_TIME_TYPE_YEAR:
        return [REPORT_CYCLE_YEAR, REPORT_CYCLE_PERIOD]
    if type in REPORT_CYCLE_PERIODS:
        return [REPORT_CYCLE_PERIOD]
    if type in REPORT_CYCLE_QUARTERS:
        return [REPORT_CYCLE_QUARTER]
    return None


def get_report_time_types(type):
    if type == REPORT_CYCLE_YEAR:
        return [REPORT_TIME_TYPE_YEAR]
    if type == REPORT_CYCLE_PERIOD:
        return REPORT_CYCLE_PERIODS
    if type == REPORT_CYCLE_QUARTER:
        return REPORT_CYCLE_QUARTERS
    return None


def get_custom_report_time_types(type):
    if type == REPORT_CYCLE_PERIOD:
        return REPORT_CYCLE_PERIODS
    if type == REPORT_CYCLE_QUARTER:
        return REPORT_CYCLE_QUARTERS
    return None


def get_custom_report_cycle_type(period):
    if period in REPORT_CYCLE_PERIODS:
        return REPORT_CYCLE_PERIOD
    return REPORT_CYCLE_QUARTER


def get_custom_report_cycle_types():
    return [REPORT_CYCLE_PERIOD, REPORT_CYCLE_QUARTER]


def get_report_cycle_types():
    return [REPORT_CYCLE_YEAR, REPORT_CYCLE_PERIOD, REPORT_CYCLE_QUARTER]


def get_period_time_types():
    return [REPORT_TIME_TYPE_YEAR, REPORT_TIME_TYPE_THREE_QUARTER, REPORT_TIME_TYPE_HALF_YEAR,
            REPORT_TIME_TYPE_FIRST_QUARTER]


def get_quarter_time_types():
    return [REPORT_TIME_TYPE_TEN_TO_TWELVE, REPORT_TIME_TYPE_SEVEN_TO_NINE,
            REPORT_TIME_TYPE_FOUR_TO_SIX, REPORT_TIME_TYPE_ONE_TO_THREE]


def get_all_report_time_types():
    return [REPORT_TIME_TYPE_YEAR, REPORT_TIME_TYPE_THREE_QUARTER, REPORT_TIME_TYPE_HALF_YEAR,
            REPORT_TIME_TYPE_FIRST_QUARTER, REPORT_TIME_TYPE_TEN_TO_TWELVE, REPORT_TIME_TYPE_SEVEN_TO_NINE,
            REPORT_TIME_TYPE_FOUR_TO_SIX, REPORT_TIME_TYPE_ONE_TO_THREE]


def get_report_types():
    return [REPORT_TYPE_BALANCE_SHEET, REPORT_TYPE_CASH_FLOW, REPORT_TYPE_PROFIT]


def get_combine_types():
    return [REPORT_BORE_COMBINE, REPORT_BORE_PARENT]


def is_basic_report_type(type):
    return type == REPORT_TYPE_BALANCE_SHEET or type == REPORT_TYPE_CASH_FLOW or type == REPORT_TYPE_PROFIT


REPORT_BORE_MAP = {
    REPORT_BORE_COMBINE: '合并',
    REPORT_BORE_PARENT: '母公司'
}


def get_report_bore_name(type):
    name = REPORT_BORE_MAP.get(type)
    if not name:
        return REPORT_BORE_MAP.get(REPORT_BORE_PARENT)
    return name


COMPARE_MEAN_MAP = {
    COMPARE_MEAN_SIMPLE: '行业算术均值',
    COMPARE_MEAN_REVENUE_WEIGHT: '按营收加权平均',
    COMPARE_MEAN_PROFIT_WEIGHT: '按利润加权平均',
    COMPARE_MEAN_ASSET_WEIGHT: '按总资产加权平均',
}


def get_compare_mean_name(type):
    name = COMPARE_MEAN_MAP.get(type)
    if not name:
        return COMPARE_MEAN_MAP.get(COMPARE_MEAN_SIMPLE)
    return name


def get_show_report_time(report_type, year, time_type):
    year = str(year)
    if time_type == REPORT_TIME_TYPE_YEAR:
        if report_type == REPORT_CYCLE_YEAR:
            return year
        return year + '全年'
    elif time_type == REPORT_TIME_TYPE_HALF_YEAR:
        return year + '半年'
    elif time_type == REPORT_TIME_TYPE_FIRST_QUARTER or time_type == REPORT_TIME_TYPE_ONE_TO_THREE:
        return year + '第一季度'
    elif time_type == REPORT_TIME_TYPE_THREE_QUARTER:
        return year + '第三季度'
    elif time_type == REPORT_TIME_TYPE_FOUR_TO_SIX:
        return year + '第二季度'
    elif time_type == REPORT_TIME_TYPE_SEVEN_TO_NINE:
        return year + '第三季度'
    elif time_type == REPORT_TIME_TYPE_TEN_TO_TWELVE:
        return year + '第四季度'
    else:
        return '-'


REPORT_CYCLE = [{'name': '年报', 'value': REPORT_CYCLE_YEAR},
                {'name': '报告期', 'value': REPORT_CYCLE_PERIOD},
                {'name': '单季度', 'value': REPORT_CYCLE_QUARTER}]

REPORT_TIME_RANGE = [{'name': '最近3年', 'value': REPORT_TIME_RANGE_THREE},
                     {'name': '最近5年', 'value': REPORT_TIME_RANGE_FIVE}]

REPORT_BORE = [{'name': '合并', 'value': REPORT_BORE_COMBINE},
               {'name': '母公司', 'value': REPORT_BORE_PARENT}]

RATIO_TYPE = [{'name': '环比', 'value': 0},
              {'name': '同比', 'value': 1}]

COMPARE_MEAN = [{'name': '行业算术均值', 'value': COMPARE_MEAN_SIMPLE},
                {'name': '按营收加权平均', 'value': COMPARE_MEAN_REVENUE_WEIGHT},
                {'name': '按利润加权平均', 'value': COMPARE_MEAN_PROFIT_WEIGHT},
                {'name': '按总资产加权平均', 'value': COMPARE_MEAN_ASSET_WEIGHT}]

TARGET_CUSTOM_INDUSTRY_VALUE = [{'name': '行业均值', 'value': TARGET_BODY_INDUSTRY_MEAN},
                                {'name': '行业中值', 'value': TARGET_BODY_INDUSTRY_MIDDLE},
                                {'name': '行业营收均值', 'value': TARGET_BODY_INDUSTRY_REVENUE_MEAN},
                                {'name': '行业利润均值', 'value': TARGET_BODY_INDUSTRY_PROFIT_MEAN},
                                {'name': '行业资产均值', 'value': TARGET_BODY_INDUSTRY_ASSET_MEAN}]

TARGET_CUSTOM_SECRET_LEVEL = [{'name': '私有', 'value': TARGET_STATUS_PRIVATE},
                              {'name': '公开', 'value': TARGET_STATUS_PUBLIC}]

TARGET_CUSTOM_STATUS = [{'name': '保存并启用', 'value': TARGET_USE},
                        {'name': '仅保存', 'value': TARGET_NO_USE}]

MONITOR_MSG_SEND_WHETHER = [{'name': '发送预警通知', 'value': TARGET_USE},
                            {'name': '暂不发送预警通知', 'value': TARGET_NO_USE}]

MONITOR_TYPE = [{'name': '财务指标', 'value': MONITOR_TYPE_FINANCE}]

COMPANY_COMPARE_TYPE = [{'name': '相邻', 'value': COMPANY_COMPARE_TYPE_NEAR},
                        {'name': '最高', 'value': COMPANY_COMPARE_TYPE_TOP},
                        {'name': '最低', 'value': COMPANY_COMPARE_TYPE_LOW}]

INDUSTRY_COMPARE_TYPE = [
    {'name': '最高', 'value': COMPANY_COMPARE_TYPE_TOP},
    {'name': '最低', 'value': COMPANY_COMPARE_TYPE_LOW}]

LIMIT_TYPE = [
    {'name': 'Top3', 'value': LIMIT_TYPE_TOP3},
    {'name': 'Top5', 'value': LIMIT_TYPE_TOP5},
    {'name': 'Top10', 'value': LIMIT_TYPE_TOP10},
]


def convert_combine_type_str_to_int(str1):
    if str1 == '001':
        return 1
    elif str1 == '002':
        return 2
    elif str1 == '003':
        return 3
    elif str1 == '004':
        return 4
    elif str1 == '005':
        return 5
    elif str1 == '006':
        return 6
    elif str1 == '007':
        return 7
    else:
        return -1


def convert_target_custom_secret_level(secret_level):
    if secret_level == TARGET_STATUS_PRIVATE:
        return '私有'
    elif secret_level == TARGET_STATUS_PUBLIC:
        return '公开'
    else:
        return '未知'


def convert_finance_target_type(target_type):
    if target_type == 1:
        return 'profit'
    elif target_type == 2:
        return 'cash_flow'
    elif target_type == 3:
        return 'balance_sheet'
    elif target_type == 4:
        return 'statistics'
    elif target_type == 5:
        return 'public_custom'
    elif target_type == 6:
        return 'private_custom'
    else:
        return 'unknown'


def get_company_risk_level(risk_score):
    if type(risk_score) == str:
        return 'yellow', '一般'
    elif 0 <= risk_score < 30:
        return 'green', '良好'
    elif 30 <= risk_score < 60:
        return 'yellow', '一般'
    else:
        return 'red', '较差'


def get_company_add_risk_level_by_income(operate_income):
    if not operate_income:
        return 0
    elif operate_income >= 50:
        return -40
    elif operate_income >= 30:
        return -30
    elif operate_income >= 20:
        return -20
    elif operate_income >= 10:
        return -10
    elif operate_income >= 3:
        return 0
    elif operate_income >= 1:
        return 10
    elif operate_income >= 0.5:
        return 20
    elif operate_income >= 0:
        return 30
    else:
        return 30


def get_risk_report_params():
    risk_report_params = {
        'profit_ability': ['operate_profit_ratio', 'netprofit_asset_ratio', 0.1, 0.15],  # 盈利能力
        'income_quality': ['profit_sustainability', 'cash_sale_ratio', 0.08, 0.05],  # 收益质量
        'cash_flow': ['cash_recovery_asset', 'cash_lq_lia', 0.15, 0.05],  # 现金流量
        'growth_ability': ['capital_accumulation_rate', 'revenue_increase_rate', 0.05, 0.05],  # 成长能力
        'capital_structure': ['asset_lia_ratio', 'lia_nettangible_asset', 0.07, 0.05],  # 资本结构
        'operate_ability': ['receivable_turnover_ratio', 'inventory_turnover_ratio', 0.02, 0.04],  # 营运能力
        'debt_ability': ['con_quick_ratio', 'times_interest_earned_ratio', 0.07, 0.07]  # 偿债能力
    }
    return risk_report_params


def get_finance_radar_key():
    return ['profit', 'grow', 'cash_flow', 'operate', 'debt', 'profit_level', 'grow_level', 'cash_flow_level',
            'operate_level', 'debt_level']
