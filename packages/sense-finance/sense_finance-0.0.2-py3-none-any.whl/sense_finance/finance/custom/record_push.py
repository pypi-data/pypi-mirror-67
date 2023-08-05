from sense_finance.finance.model import *
from sense_finance.finance.target.base import BaseTargetComputer
from sense_finance.finance.custom.new_update import NewCustomTargetUpdater


class RecordPushHandler(BaseTargetComputer):
    __target_map = dict()
    __last_load_target_time = 0

    def __init__(self):
        super(RecordPushHandler, self).__init__()

    def delete_sensedeal_record(self, report_no):
        if not report_no:
            return
        self.report_data_dao.delete_record_by_no(report_no)

    @classmethod
    def check_target_map(cls):
        diff = sd.get_current_second() - cls.__last_load_target_time
        if diff < 3600 * 24:
            return cls.__target_map
        items = ReportModel.find_all()
        sd.log_info("load report model size={}".format(len(items)))
        for item in items:
            if not item.is_valid():
                continue
            key = "{0}_{1}_{2}".format(item.model_class, item.model_no, item.row_name_sensedeal)
            cls.__target_map[key] = item
        sd.log_info("done _check_target_map")
        cls.__last_load_target_time = sd.get_current_second()
        return cls.__target_map

    def get_target(self, report_record, field):
        target_map = RecordPushHandler.check_target_map()
        key = "{0}_{1}_{2}".format(report_record.model_class, report_record.model_no, field)
        return target_map.get(key)

    def _select_old_record(self, report_record):
        record = ReportRecord.objects.filter(company_code=report_record.company_code,
                                             report_scope=report_record.report_scope,
                                             report_year=report_record.report_year,
                                             report_period=report_record.report_period,
                                             model_no=report_record.model_no).first()
        if not record:
            report_record.save()
            sd.log_info("save new report_record {0} no={1}".format(report_record.id, report_record.report_no))
            return report_record, None
        data_list = ReportData.objects.filter(report_record_id=record.id).all()
        return record, data_list

    def update_record(self, data):
        sd.log_info("start update_record data={}".format(data))
        report_record, num = self._update_record_data(data)
        if num == 0:
            sd.log_warn("no change update for data = {}".format(data))
        return report_record, num

    @sd.try_catch_exception
    def update_custom_target(self, record):
        updater = NewCustomTargetUpdater()
        updater.update_record(record)

    def build_update_record_data(self, id):
        record = ReportRecord.find_by_id(id)
        report_record, old_data_list = self._select_old_record(record)
        report_record.report_datas = old_data_list
        return report_record, len(old_data_list)

    def _update_record_data(self, data):
        attrs = data.get('attrs')
        if not attrs:
            sd.log_error("invalid data format {}".format(data))
            return None, 0
        del data['attrs']
        record = ReportRecord(**data)
        report_record, old_data_list = self._select_old_record(record)
        if not old_data_list:
            old_data_map = dict()
        else:
            old_data_map = {data.report_model_id: data for data in old_data_list}
        inserts = list()
        updates = list()
        for field, val in attrs.items():
            model = self.get_target(report_record, field)
            if not model:
                sd.log_error("null target for model_class={0},model_no={1},field={2}".format(report_record.model_class,
                                                                                             report_record.model_no,
                                                                                             field))
                continue
            if val is None:
                continue
            old_data = old_data_map.get(model.id)
            if not old_data:
                report_data = ReportData()
                report_data.report_record_id = report_record.id
                report_data.report_model_id = model.id
                report_data.value = val
                inserts.append(report_data)
            elif old_data.value != val:
                old_data.value = val
                updates.append(old_data)
        if updates:
            for data in updates:
                data.save()
        if inserts:
            ReportData.objects.bulk_create(inserts)
        report_record.report_datas = inserts + updates
        sd.log_info(
            "handle_update_report_record record {0} data insert size={1} for company {2} report={3} update size={4} total={5}".format(
                report_record.id,
                len(inserts),
                report_record.company_code,
                report_record.report_no, len(updates), len(report_record.report_datas)))
        return report_record, len(report_record.report_datas)
