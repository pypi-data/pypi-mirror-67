from sense_finance.finance.helper import *
from .base import BaseCondition
from sense_finance.finance.common.constants import *
from sense_finance.finance.common import get_report_time_range


class TargetCondition(BaseCondition):

    def __init__(self, report_time_type=None, time_range_type=None, compare_type=None, company=None, company_list=None,
                 targets=None, combine_type=None, limit_type=None, compare_target=None, start_year=None, end_year=None,
                 model_class=None, report_time_types=None, user_id=0, industry_id=None, max_size=0, report_record=None,
                 check_year_range=False):
        super(TargetCondition, self).__init__(company=company, company_list=company_list,
                                              targets=targets, combine_type=combine_type, compare_target=compare_target,
                                              user_id=user_id, industry_id=industry_id)
        self.report_time_type = report_time_type
        self.time_range_type = time_range_type
        self.compare_type = compare_type
        self.max_size = max_size
        self.report_record = report_record
        self.check_year_range = check_year_range
        if start_year is None and end_year is None:
            self.start_year, self.end_year = get_report_time_range(time_range_type)
        else:
            self.start_year = start_year
            self.end_year = end_year
        if targets:
            self.target_map = {target.name: target for target in targets}
        else:
            self.target_map = dict()
        self.custom_target_map = dict()
        self.select_start_year = self.start_year
        self.select_end_year = self.end_year
        if self.company_list:
            self.company_ids = [x.company_code for x in self.company_list]
        else:
            self.company_ids = list()
        self.limit_type = limit_type
        self.model_class = model_class
        self.report_time_types = report_time_types
        if self.report_time_types is None and report_time_type is not None:
            self.report_time_types = get_report_time_types(report_time_type)
        self.ratio_type = 0

    def get_record_limit(self):
        ratio = 4
        if self.report_time_type == REPORT_CYCLE_YEAR:
            ratio = 1
        if self.time_range_type == REPORT_TIME_RANGE_THREE:
            return ratio * 3
        return ratio * 5

    def __str__(self):
        return "TargetCondition(report_time_type={0},time_range_type={1},compare_type={2},start_year={3},end_year={4})".format(
            self.report_time_type, self.time_range_type, self.compare_type, self.start_year, self.end_year)
