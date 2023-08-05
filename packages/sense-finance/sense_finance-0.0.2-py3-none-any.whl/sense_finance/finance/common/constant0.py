INDUSTRY_LEVEL_FIRST = 1
INDUSTRY_LEVEL_SECOND = 2
INDUSTRY_LEVEL_THIRD = 3
INDUSTRY_LEVEL_FOUR = 4

PUSH_COMPANY_ON_MARKET = 1
PUSH_COMPANY_NOT_MARKET = 2
PUSH_COMPANY_RELATED = 3
PUSH_COMPANY_SITE = 4

PUSH_TYPE_FINANCE = 1
PUSH_TYPE_EVENT = 2
PUSH_TYPE_TRANSMIT = 3
PUSH_TYPE_DEBT = 4

TASK_TYPE_CUSTOM_TARGET = 1
TASK_TYPE_CUSTOM_MONITOR = 2
TASK_TYPE_LOG = 3
TASK_TYPE_USER_NOTICE = 4
TASK_TYPE_BENCHMARK = 5

NOTICE_TYPE_CUSTOM_TARGET = 1
NOTICE_TYPE_CUSTOM_MONITOR = 2

NOTICE_ACTION_UPDATE = 1
NOTICE_ACTION_DELETE = 2
NOTICE_ACTION_CLOSE = 3

TASK_ACTION_ADD = 1
TASK_ACTION_DELETE = 2
TASK_ACTION_UPDATE = 3

TASK_ACTION_UPDATE_TARGET = 3
TASK_ACTION_UPDATE_MONIT = 4
TASK_ACTION_DELETE_MONIT = 5
TASK_ACTION_CLOSE_MONIT = 6


def get_industry_level(industry_id):
    if len(industry_id) == 1:
        return INDUSTRY_LEVEL_FIRST
    if len(industry_id) == 2:
        return INDUSTRY_LEVEL_SECOND
    if len(industry_id) == 3:
        return INDUSTRY_LEVEL_THIRD
    if len(industry_id) == 4:
        return INDUSTRY_LEVEL_FOUR
    return None


def is_sensedeal_company(company_code):
    return len(company_code) <= 8 or company_code.find('10000') == 0


def get_sensedeal_company_codes(company_codes):
    return [code for code in company_codes if code]


FINANCE_DB = 'fengmi'


def table_name(name):
    return name
