from sense_finance.finance.common import FINANCE_DB, table_name
from sense_finance.finance.common import *
from sense_finance.finance.util import *
from sense_finance.finance.model.base import *


class BaseReportRecord(BaseModel):
    class Meta:
        abstract = True

    @property
    def report_datas(self):
        return getattr(self, '_report_datas', None)

    @report_datas.setter
    def report_datas(self, info):
        setattr(self, '_report_datas', info)

    @property
    def report_real_month(self):
        if self.report_month is None:
            self.report_month = get_report_month(self.report_period)
        return self.report_month

    def get_combine_type(self):
        return self.report_scope

    def get_cycle_type(self):
        return get_custom_report_cycle_type(self.report_period)

    def custom_key(self):
        return "{0}_{1}_{2}_{3}_{4}".format(self.company_code, self.report_scope, self.report_period, self.model_class,
                                            self.report_year)


class ReportRecord(BaseReportRecord):
    id = models.AutoField(primary_key=True)
    report_no = models.CharField(max_length=50, blank=True, null=True)
    company_code = models.CharField(max_length=50, blank=True, null=True)
    report_scope = models.IntegerField(blank=True, null=True)
    report_period = models.IntegerField(blank=True, null=True)
    model_class = models.CharField(max_length=20, blank=True, null=True)
    model_no = models.IntegerField(blank=True, null=True)
    report_name = models.CharField(max_length=200, blank=True, null=True)
    report_year = models.IntegerField(blank=True, null=True)
    report_month = models.IntegerField(blank=True, null=True)
    report_currency = models.CharField(max_length=2, blank=True, null=True, default=10)
    report_rate = models.FloatField(blank=True, null=True, default=0)

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_report_record')

    def __str__(self):
        return "ReportRecord(id={0},company_code={1},report_scope={2},report_period={3},model_class={4},model_no={5},report_name={6},report_year={7}".format(
            self.id, self.company_code, self.report_scope, self.report_period, self.model_class, self.model_no,
            self.report_name, self.report_year)

    def check_valid(self, record):
        if self.company_code != record.company_code or self.report_scope != record.report_scope or self.model_class != record.model_class or self.model_no != record.model_no or self.report_year != record.report_year or self.report_month != record.report_month:
            return -1
        if self.report_name != record.report_name or self.report_no != record.report_no or self.report_currency != record.report_currency or self.report_rate != record.report_rate:
            return 0
        return 1

    def data_type(self):
        return COMPANY_TYPE_SENSEDEAL

    @property
    def key(self):
        return "s_{}".format(self.id)

    def is_custom(self):
        return False


class CustomReportRecord(BaseReportRecord):
    id = models.AutoField(primary_key=True)
    report_no = models.CharField(max_length=50, blank=True, null=True)
    company_code = models.CharField(max_length=50, blank=True, null=True)
    report_scope = models.IntegerField(blank=True, null=True)
    report_period = models.IntegerField(blank=True, null=True)
    model_class = models.CharField(max_length=20, blank=True, null=True)
    model_no = models.IntegerField(blank=True, null=True)
    report_name = models.CharField(max_length=200, blank=True, null=True)
    report_year = models.IntegerField(blank=True, null=True)
    report_month = models.IntegerField(blank=True, null=True)
    report_currency = models.CharField(max_length=2, blank=True, null=True, default=10)
    report_rate = models.FloatField(blank=True, null=True, default=0)

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_custom_report_record')

    def __str__(self):
        return "CustomReportRecord(id={0},company_code={1},report_scope={2},report_period={3},model_class={4},model_no={5},report_name={6},report_year={7}".format(
            self.id, self.company_code, self.report_scope, self.report_period, self.model_class, self.model_no,
            self.report_name, self.report_year)

    def __repr__(self):
        return self.__str__()

    @property
    def key(self):
        return "c_{}".format(self.id)

    def data_type(self):
        return COMPANY_TYPE_CUSTOM

    def is_custom(self):
        return True


def get_report_record_class(company_code):
    return ReportRecord


def get_sensedeal_record_ids(items):
    return [item.id for item in items if item.data_type() == COMPANY_TYPE_SENSEDEAL]


def get_custom_record_ids(items):
    return [item.id for item in items if item.data_type() == COMPANY_TYPE_CUSTOM]
