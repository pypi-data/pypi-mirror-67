from .base import BaseTargetComputer
from sense_finance.finance.dao import *
from sense_finance.finance.model import *
from sense_finance.finance.util import strip_industry_id



class TargetLatestDataHandler(BaseTargetComputer):

    def __init__(self):
        super(TargetLatestDataHandler, self).__init__()
        self.update_count = 0

    @sd.try_catch_exception
    def _update_latest_data(self, company, record, report_data, latest_data, report_scope, report_cycle,
                            new_latest_data_list):
        value = report_data.real_value(record)
        if not latest_data:
            latest_data = CompanyTargetLatestData(company_code=record.company_code, report_scope=report_scope,
                                                  report_model_id=report_data.report_model_id,
                                                  report_cycle=report_cycle,
                                                  report_period=record.report_period,
                                                  report_year=record.report_year, value=value)
            latest_data.first_industry_code = strip_industry_id(company.first_industry_code)
            latest_data.second_industry_code = strip_industry_id(company.second_industry_code)
            latest_data.three_industry_code = strip_industry_id(company.three_industry_code)
            latest_data.four_industry_code = strip_industry_id(company.four_industry_code)
            new_latest_data_list.append(latest_data)
            return latest_data
        if not self._is_better_latest_data(record, report_data, latest_data):
            return latest_data
        latest_data.report_period = record.report_period
        latest_data.report_year = record.report_year
        latest_data.value = value
        if latest_data.id:
            latest_data.save()
            sd.log_info("update latest_data={0}".format(latest_data))
            self.update_count += 1
        return latest_data

    def update_by_company_code(self, record_map, report_datas, company, report_scope, report_cycle, latest_data_map,
                               need_save=True):
        company_code = company.company_code
        model_data_map = dict()
        for report_data in report_datas:
            report_data2 = model_data_map.get(report_data.report_model_id)
            if not report_data2:
                model_data_map[report_data.report_model_id] = report_data
                continue
            record1 = record_map[report_data.report_record_id]
            record2 = record_map[report_data2.report_record_id]
            if self._is_better_record(record1, record2):
                model_data_map[report_data.report_model_id] = report_data

        new_latest_data_list = list()
        for report_data in model_data_map.values():
            record = record_map[report_data.report_record_id]
            key = CompanyTargetLatestData.get_key(company_code, report_scope, report_cycle, report_data.report_model_id)
            latest_data = self._update_latest_data(company, record, report_data, latest_data_map.get(key), report_scope,
                                                   report_cycle, new_latest_data_list)
            latest_data_map[key] = latest_data
        if len(new_latest_data_list) > 0 and need_save:
            CompanyTargetLatestData.batch_save(new_latest_data_list)
            sd.log_info(
                "CompanyTargetLatestData save new size={2} for company_code={0} report_scope={1}".format(
                    company_code,
                    report_scope, len(new_latest_data_list)))
        return new_latest_data_list

    def _is_better_record(self, record1, record2):
        flag = self._get_record_flag(record1, record2)
        if flag == 1:
            return True
        return False

    def _get_record_flag(self, record1, record2):
        if record1.report_year > record2.report_year:
            return 1
        if record1.report_year < record2.report_year:
            return -1
        if record1.report_period > record2.report_period:
            return 1
        if record1.report_period < record2.report_period:
            return -1
        return 0

    def _is_better_latest_data(self, record, report_data, latest_data):
        flag = self._get_record_flag(record, latest_data)
        if flag == 1:
            return True
        if flag == -1:
            return False
        value = report_data.real_value(record)
        if latest_data.value != value:
            if abs(latest_data.value - value) > 0.0001:
                return True
        return False
