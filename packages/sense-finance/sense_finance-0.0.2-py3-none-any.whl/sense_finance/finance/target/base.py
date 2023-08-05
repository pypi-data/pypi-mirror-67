from sense_finance.finance.dao import *
from sense_finance.finance.model import is_invalid_target_val


class BaseTargetComputer(object):

    def __init__(self):
        self.target_dao = TargetDAO()
        self.industry_dao = IndustryDAO()
        self.target_data_dao = TargetDataDAO()
        self.industry_data_dao = IndustryDataDAO()
        self.company_dao = CompanyDAO()
        self.finance_company_dao = FinanceCompanyDAO()
        self.report_data_dao = ReportDataDAO()
        self.report_time_items = list()
        self.report_select_time_items = list()
        self.target_container = None

    def get_target_record_models(self, targets):
        has_custom = False
        has_normal = False
        for target in targets:
            if target.is_custom:
                has_custom = True
            else:
                has_normal = True
        models = list()
        if has_custom:
            models.append(CustomReportRecord)
        if has_normal:
            models.append(ReportRecord)
        return models

    def check_target_condition(self, condition):
        pass

    def refine_target_value(self, val):
        if val > 1000:
            return str(round(val, 0))
        if val >= 1:
            return str(round(val, 2))
        return str(round(val, 4))

    def get_target_value_way_ratio(self, val, val1):
        if is_invalid_target_val(val) or is_invalid_target_val(val1) or val is None or val1 is None:
            return WAY_NO, ""
        diff = val - val1
        if val1 != 0:
            ratio = "{:.2f}%".format(abs(diff * 100.0 / val1))
        else:
            ratio = ''
        if diff > 0:
            return WAY_UP, ratio
        elif diff < 0:
            return WAY_DOWN, ratio
        return WAY_NO, ""

    def build_report_time_items(self, condition, target_container):
        size_limit = condition.get_record_limit()
        record_items = target_container.record_items
        if record_items and record_items[0].report_year < condition.end_year:
            condition.start_year = condition.start_year - (condition.end_year - record_items[0].report_year)
            last_report_year = record_items[len(record_items) - 1].report_year
            if condition.start_year < last_report_year:
                condition.start_year = last_report_year
            if condition.select_start_year > last_report_year:
                condition.select_start_year = last_report_year
        start_year = condition.start_year
        self._build_report_time_items0(self.report_time_items, condition, target_container, size_limit,
                                       start_year)
        self._build_report_time_items0(self.report_select_time_items, condition, target_container, size_limit + 1,
                                       start_year - 1)

    def _build_report_time_items0(self, report_time_items, condition, target_container, size_limit, start_year):
        time_types = get_report_time_types(condition.report_time_type)
        for year in range(condition.end_year, start_year, -1):
            for time_type in time_types:
                key = get_report_time_key(year, time_type)
                if not target_container.has_time_data_items(key) and not report_time_items:
                    continue
                report_time_items.append((year, time_type))
                if len(report_time_items) >= size_limit:
                    break
        sd.log_info(
            "build_report_time_items={0},end_year={1},start_year={2} size_limit={3}".format(report_time_items, condition.end_year,
                                                                             start_year,size_limit))
