import sense_core as sd
from sense_finance.finance.util import *
from sense_finance.finance.work.base_worker import BaseWorker
from sense_finance.finance.model import *
from sense_finance.finance.custom import RecordPushHandler
from sense_finance.finance.target import ComapnyModelClassManager, TargetLatestDataUpdater2, IndustryTargetUpdater


class SenseSyncHandler(BaseWorker):

    def __init__(self, is_init=False):
        self.is_init = is_init

    @sd.try_catch_exception
    def consume_queue(self):
        sd.log_info("start consume_queue")
        consumer = sd.RabbitConsumer2(topic='fengmi_finance_record', label='rabbit_finance')
        consumer.consume_loop(self.handle_message)

    def handle_delete_report_record(self, data):
        handler = RecordPushHandler()
        handler.delete_sensedeal_record(data.get('report_no'))

    def handle_update_report_record(self, data):
        sd.log_info("start handle_update_report_record {}".format(data))
        handler = RecordPushHandler()
        report_record, num = handler.update_record(data)
        if not report_record:
            return
        if num > 0 and not self.is_init:
            self._handle_update_related(report_record)
        sd.log_info("done handle_update_report_record {}".format(data))

    def _handle_update_related(self, report_record):
        if report_record.report_year >= get_current_year() - 1:
            industry_updater = IndustryTargetUpdater()
            industry_updater.update_record(report_record)
        handler = RecordPushHandler()
        handler.update_custom_target(report_record)
        manager = ComapnyModelClassManager()
        manager.check_model_class(report_record)
        target_data_handler = TargetLatestDataUpdater2()
        target_data_handler.update_record(report_record)

    def handle_message(self, message):
        data = sd.load_json(message)
        action = data.get('action')
        table = data.get('table')
        data = data.get('data')
        if table != 'report_record' or not data:
            sd.log_error("invali data {}".format(message))
            return
        if action == "+":
            self.handle_update_report_record(data)
        elif action == '-':
            self.handle_delete_report_record(data)
