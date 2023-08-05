from sense_finance.finance.model import *
from sense_finance.finance.helper import *
from django.db.utils import IntegrityError
from sense_finance.finance.common import *


class ReportDataDAO(object):

    def find_industry_latest_target_data(self, industry_level, industry_id, report_scope, report_cycle, target_id):
        objects = CompanyTargetLatestData.objects.filter(report_model_id=target_id, report_scope=report_scope,
                                                         report_cycle=report_cycle)
        if industry_level == INDUSTRY_LEVEL_FIRST:
            objects = objects.filter(first_industry_code=industry_id).all()
        elif industry_level == INDUSTRY_LEVEL_SECOND:
            objects = objects.filter(second_industry_code=industry_id).all()
        elif industry_level == INDUSTRY_LEVEL_THIRD:
            objects = objects.filter(three_industry_code=industry_id).all()
        elif industry_level == INDUSTRY_LEVEL_FOUR:
            objects = objects.filter(four_industry_code=industry_id).all()
        items = list(objects)
        sd.log_info("find_industry_latest_target_data industry_level={0},industry_id={1},len={2}".format(industry_level,
                                                                                                         industry_id,
                                                                                                         len(items)))
        return items

    def find_latest_target_data(self, company_codes, report_scope, report_cycle, target_id):
        start_time = sd.get_current_millisecond()
        result = list()
        unit = 1000
        total = len(company_codes)
        for i in range(int(total / unit) + 1):
            if i * unit >= total:
                break
            if total < (i + 1) * unit:
                ids = company_codes[i * unit:total]
            else:
                ids = company_codes[i * unit:(i + 1) * unit]
            items = list(
                CompanyTargetLatestData.objects.filter(report_model_id=target_id, report_scope=report_scope,
                                                       report_cycle=report_cycle, company_code__in=ids).all())
            sd.log_info("{0}={1}".format(ids, len(items)))
            result.extend(items)
        cost = sd.get_current_millisecond() - start_time
        sd.log_info(
            "find_latest_target_data size={0} company_codes={1} for report_scope={2} report_cycle={3} target_id={4} cost={5}".format(
                len(result),
                len(company_codes),
                report_scope,
                report_cycle,
                target_id, cost))
        return result

    def delete_record_by_no(self, report_no):
        record = ReportRecord.objects.filter(report_no=report_no).first()
        if not record:
            sd.log_info("not found delete record report_no = {}".format(report_no))
            return
        ReportData.objects.filter(report_record_id=record.id).delete()
        CustomReportData.objects.filter(report_record_id=record.id).delete()
        record.delete()
        sd.log_info("done delete_record_by_no {}".format(report_no))

    def make_sure_custom_record(self, record):
        custom_record = self._find_custom_record(record)
        if custom_record:
            return custom_record
        return self.save_custom_record(record)

    def _find_custom_record(self, record):
        return CustomReportRecord.objects.filter(company_code=record.company_code,
                                                 report_scope=record.report_scope,
                                                 report_period=record.report_period,
                                                 model_class=record.model_class,
                                                 report_year=record.report_year).first()

    def save_custom_record(self, record):
        try:
            custom_record = CustomReportRecord(company_code=record.company_code, report_scope=record.report_scope,
                                               report_period=record.report_period, model_class=record.model_class,
                                               report_year=record.report_year, report_month=record.report_month)
            sd.log_info("save CustomReportRecord:{}".format(custom_record))
            custom_record.save()
            return custom_record
        except IntegrityError as ex:
            return self._find_custom_record(record)

    def find_company_custom_records(self, company_code):
        return list(CustomReportRecord.objects.filter(company_code=company_code).all())

    def find_latest_record(self, company_code):
        record_class = self._get_record_class(get_company_type(company_code))
        return record_class.objects.filter(company_code=company_code).order_by('-report_year', '-id').first()

    def find_latest_records(self, company_code, report_scope, limit):
        record_class = self._get_record_class(get_company_type(company_code))
        return record_class.objects.filter(company_code=company_code, report_scope=report_scope).order_by(
            '-report_year', '-id').all()[0:limit]

    def get_company_record_class(self, company_code):
        return self._get_record_class(get_company_type(company_code))

    def _get_record_class(self, data_type):
        return ReportRecord

    def find_by_records_model_ids(self, record_ids, model_ids, data_class):
        result = list()
        unit = 1000
        total = len(record_ids)
        for i in range(int(total / unit) + 1):
            if i * unit >= total:
                break
            if total < (i + 1) * unit:
                ids = record_ids[i * unit:total]
            else:
                ids = record_ids[i * unit:(i + 1) * unit]
            items = self._find_by_records_model_ids0(ids, model_ids, data_class)
            result.extend(items)
        sd.log_info(
            "find_by_records_model_ids size={0} record_ids={1} for model_ids {2} data_class={3}".format(len(result),
                                                                                                        len(record_ids),
                                                                                                        model_ids,
                                                                                                        data_class))
        return result

    def _find_by_records_model_ids0(self, record_ids, model_ids, data_class):
        if model_ids:
            if len(model_ids) == 1:
                items = list(
                    data_class.objects.filter(report_model_id=model_ids[0], report_record_id__in=record_ids).all())
            else:
                items = list(
                    data_class.objects.filter(report_record_id__in=record_ids, report_model_id__in=model_ids).all())
        else:
            items = list(
                data_class.objects.filter(report_record_id__in=record_ids).all())
        sd.log_info(
            "_find_by_records_model_ids record_id={0} model_ids={1} data_class={2} size={3}".format(len(record_ids),
                                                                                                    model_ids,
                                                                                                    data_class,
                                                                                                    len(items)))
        return items

    # 需要测试逻辑
    def find_by_record_model(self, records, targets=None):
        result = list()
        basic_targets = get_basic_targets(targets)
        sense_record_ids = get_sensedeal_record_ids(records)
        custom_record_ids = get_custom_record_ids(records)
        if basic_targets or not targets:
            model_ids = [target.id for target in basic_targets if target.id > 0]
            if sense_record_ids:
                result.extend(self.find_by_records_model_ids(sense_record_ids, model_ids, ReportData))
        custom_targets = get_custom_targets(targets)
        if sd.is_debug():
            sd.log_info("custom_targets={}".format(custom_targets))
        if custom_targets or not targets:
            model_ids = [target.id for target in custom_targets if target.id > 0]
            if custom_record_ids:
                result.extend(self.find_by_records_model_ids(custom_record_ids, model_ids, CustomReportData))
        target_size = len(targets) if targets else 0
        sd.log_info(
            "find_by_record_model size={1} for records={1} targets={2} custom_record_ids={3} sense_record_ids={4} custom_targets={5}".format(
                len(result), len(records), target_size, len(custom_record_ids), len(sense_record_ids),
                len(custom_targets)))
        return result
