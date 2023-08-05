import datetime
from .constants import *


def get_report_time_range(type):
    year = datetime.datetime.now().year
    return year - get_report_time_range_value(type), year


def get_report_time_range_value(type):
    if type == REPORT_TIME_RANGE_CURRENT:
        return 0
    if type == REPORT_TIME_RANGE_ONE:
        return 1
    if type == REPORT_TIME_RANGE_TWO:
        return 2
    if type == REPORT_TIME_RANGE_THREE:
        return 3
    if type == REPORT_TIME_RANGE_FIVE:
        return 5
    return 6


def get_report_time_key(report_year, report_time_type):
    return "{0}_{1}".format(report_year, report_time_type)
