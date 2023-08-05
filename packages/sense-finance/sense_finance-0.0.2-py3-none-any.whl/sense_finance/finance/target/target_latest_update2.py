from sense_finance.finance.dao import *
from sense_finance.finance.model import *
from .target_latest_handler import TargetLatestDataHandler
from .base_update import BaseTargetUpdater
import gc



class TargetLatestDataUpdater2(BaseTargetUpdater):

    def __init__(self):
        super(TargetLatestDataUpdater2, self).__init__()
        self.latest_datas = list()
        self.new_latest_datas = list()

    @sd.try_catch_exception
    def update_target_id(self, target_id):
        target = TargetDAO().find_target(target_id)
        self.update_target(target)

    @sd.try_catch_exception
    def clear_data(self):
        super(TargetLatestDataUpdater2, self).clear_data()
        if self.latest_datas:
            del self.latest_datas
        if self.new_latest_datas:
            del self.new_latest_datas

    @sd.try_catch_exception
    def delete_custom_target(self, id):
        sd.log_info("start delete_custom_target latest data {}".format(id))
        CompanyTargetLatestData.objects.filter(report_model_id=id).delete()
        sd.log_info("done delete_custom_target latest data {}".format(id))

    def load_target_latest_data(self, target):
        items = list(CompanyTargetLatestData.objects.filter(report_model_id=target.id).all())
        sd.log_info("load CompanyTargetLatestData size={0} for target={1}".format(len(items), target.id))
        self.latest_datas = items
        self.old_count = len(items)

    @sd.try_catch_exception
    def update_all(self, thread_num=4, mod_index=1, mod_size=1):
        start_time = sd.get_current_second()
        sd.log_info(
            "start update_all target_latest mod_index={0} mod_size={1} thread_num={2}".format(mod_index, mod_size,
                                                                                              thread_num))
        close_model_connection()
        self.load_record_map()
        self.update_normal_targets(thread_num, mod_index, mod_size)
        self.update_custom_targets(thread_num, mod_index, mod_size)
        self.clear_data()
        sd.log_info(
            "done update_all target_latest cost={0}".format(sd.get_current_second() - start_time))

    @sd.try_catch_exception
    def update_custom_targets(self, thread_num=4, mod_index=1, mod_size=1):
        targets = list(CustomTarget.objects.all())
        sd.log_info("get custom_targets size = {}".format(len(targets)))
        if mod_size > 1:
            targets = [target for target in targets if target.id % mod_size == mod_index]
        sd.log_info(
            "start update_custom_targets  target size={0} mod_index={1} mod_size={2}".format(len(targets), mod_index,
                                                                                             mod_size))
        for target in targets:
            self.update_target(target, thread_num)
            close_model_connection()
            gc.collect()
        sd.log_info(
            "done update_custom_targets  target size={0} mod_index={1} mod_size={2}".format(len(targets), mod_index,
                                                                                            mod_size))

    @sd.try_catch_exception
    def update_normal_targets(self, thread_num=4, mod_index=1, mod_size=1):
        targets = list(ReportModel.objects.filter(row_name_normal__isnull=False).all())
        sd.log_info("get ReportModel size = {}".format(len(targets)))
        if mod_size > 1:
            targets = [target for target in targets if target.id % mod_size == mod_index]
        sd.log_info(
            "start update_normal_targets  target size={0} mod_index={1} mod_size={2}".format(len(targets), mod_index,
                                                                                             mod_size))
        for target in targets:
            self.update_target(target, thread_num)
            close_model_connection()
        sd.log_info(
            "done update_normal_targets  target size={0} mod_index={1} mod_size={2}".format(len(targets), mod_index,
                                                                                            mod_size))

    @sd.try_catch_exception
    def update_target(self, target, thread_num=4):
        sd.log_info("start target_latest_data for target={0}".format(target.id))
        self.new_count, self.old_count, self.update_count = 0, 0, 0
        self.new_latest_datas = list()
        if not target.need_update_industry():
            sd.log_info("no need update_target latest value for {0}".format(target.name))
            return True
        start_time = sd.get_current_second()
        self.load_record_map(target)
        self.load_targets_data([target])
        self.load_target_latest_data(target)
        companys = CompanyDAO().get_finance_all(model_class=target.model_class)
        sd.log_info("got CompanyInfo size={0}".format(len(companys)))
        items = [{
            'target': target,
            'company': company,
        } for company in companys]
        time1 = sd.get_current_second()
        sd.execute_multi_core('update_target', self._update_thread_target, items, thread_num, True)
        sd.log_info(
            "done update_target batch for target={0} cost={1}".format(target.id, sd.get_current_second() - time1))
        self._save_new_data(target)
        sd.log_info(
            "done target_latest_data update_custom_target cost={0} companys={1} new_count={2} old_count={3} update_count={4} target={5}".format(
                sd.get_current_second() - start_time, len(companys), self.new_count, self.old_count, self.update_count,
                target.id))
        return True

    def _update_thread_target(self, item):
        self.update_by_company_code(item['company'], item['target'])

    def update_by_company_code(self, company, target=None):
        record_map = None
        data_items = None
        target_id = 0
        if target:
            record_items = self.company_record_map.get(company.company_code)
            data_items = self.company_data_map.get(company.company_code)
            if not record_items or not data_items:
                sd.log_info("update_by_company_code {0} not data".format(company.company_code))
                return
            target_id = target.id
            record_map = {record.key: record for record in record_items}
        self.update_by_company_code_report_scope(company, REPORT_BORE_COMBINE, target, record_map, data_items)
        self.update_by_company_code_report_scope(company, REPORT_BORE_PARENT, target, record_map, data_items)
        sd.log_info("done update_by_company_code1 company_code={0} target_id={1}".format(
            company.company_code, target_id))

    @sd.try_catch_exception
    def update_record(self, record):
        sd.log_info("start target_latest update_record for record {0}".format(record.id))
        company = self.company_dao.get_company(record.company_code)
        if not company:
            return
        if record.report_period == REPORT_TIME_TYPE_YEAR:
            self.update_record0(company, record, REPORT_CYCLE_YEAR)
        if record.report_period in get_period_time_types():
            self.update_record0(company, record, REPORT_CYCLE_PERIOD)
        if record.report_period in get_quarter_time_types():
            self.update_record0(company, record, REPORT_CYCLE_QUARTER)
        sd.log_info("done target_latest update_record for record {0}".format(record))

    def update_record0(self, company, record, report_cycle):
        self.update_by_company_code_report_scope_cycle(company, record.report_scope, report_cycle, record=record)

    def update_by_company_code_report_scope(self, company, report_scope, target=None, record_map=None, data_items=None):
        self.update_by_company_code_report_scope_cycle(company, report_scope, REPORT_CYCLE_YEAR, target,
                                                       record_map=record_map, data_items=data_items)
        self.update_by_company_code_report_scope_cycle(company, report_scope, REPORT_CYCLE_PERIOD, target,
                                                       record_map=record_map, data_items=data_items)
        self.update_by_company_code_report_scope_cycle(company, report_scope, REPORT_CYCLE_QUARTER, target,
                                                       record_map=record_map, data_items=data_items)

    def _get_latest_data(self, company_code, target, report_scope, report_cycle):
        if target:
            latest_datas = self.latest_datas
        else:
            latest_datas = None
        if latest_datas:
            datas = list()
            for data in latest_datas:
                if data.report_scope == report_scope and data.report_cycle == report_cycle:
                    datas.append(data)
        else:
            objects = CompanyTargetLatestData.objects.filter(company_code=company_code,
                                                             report_scope=report_scope,
                                                             report_cycle=report_cycle)
            if target:
                objects = objects.filter(report_model_id=target.id)
            datas = objects.all()
        latest_data_map = {data.key(): data for data in datas}
        return latest_data_map

    def update_by_company_code_report_scope_cycle(self, company, report_scope, report_cycle, target=None,
                                                  record=None, record_map=None, data_items=None):
        company_code = company.company_code
        latest_data_map = self._get_latest_data(company_code, target, report_scope, report_cycle)
        target_id = target.id if target else ""
        record_id = record.id if record else ""
        self._update_by_company_code(company, report_scope, report_cycle, latest_data_map, target,
                                     record, record_map=record_map, data_items=data_items)
        if not self.latest_datas:
            sd.log_info(
                "done update_by_company_code_report_scope_cycle company_code={0} report_scope={1} report_cycle={2} record_id={3} target_id={4} old={5}".format(
                    company_code, report_scope, report_cycle, record_id, target_id, len(latest_data_map)))

    @sd.try_catch_exception
    def _save_new_data(self, target):
        time = sd.get_current_second()
        CompanyTargetLatestData.batch_save(self.new_latest_datas)
        self.new_count = len(self.new_latest_datas)
        sd.log_info("_save_new_data size={0} for target={1} cost={2}".format(self.new_count, target.id,
                                                                             sd.get_current_second() - time))

    def _get_company_record_datas(self, report_scope, report_cycle, record_map, data_items):
        report_time_types = get_report_time_types(report_cycle)
        records = list()
        datas = list()
        for data in data_items:
            record = record_map[data.record_key]
            if record.report_scope == report_scope and record.report_period in report_time_types:
                records.append(record)
                datas.append(data)
        return records, datas

    def _update_by_company_code(self, company, report_scope, report_cycle, latest_data_map,
                                target=None, record=None, record_map=None, data_items=None):
        company_code = company.company_code
        if not record:
            need_save = False
            records, datas = self._get_company_record_datas(report_scope, report_cycle, record_map, data_items)
        else:
            need_save = True
            targets = [target] if target else None
            records = [record]
            datas = self.report_data_dao.find_by_record_model(records, targets)
        if not records or not datas:
            return
        record_map = {record.id: record for record in records}
        if not self.latest_datas:
            sd.log_info(
                "report_datas size={0} for company_code={1} report_scope={2} report_cycle={3}".format(len(datas),
                                                                                                      company_code,
                                                                                                      report_scope,
                                                                                                      report_cycle))
        handler = TargetLatestDataHandler()
        new_datas = handler.update_by_company_code(record_map, datas, company, report_scope, report_cycle,
                                                   latest_data_map, need_save=need_save)
        if need_save:
            return
        self.update_count += handler.update_count
        if new_datas:
            self.new_latest_datas.extend(new_datas)
