import sense_core as sd
from sense_finance.finance.util import *
from sense_finance.finance.common import FINANCE_DB, table_name
from sense_finance.finance.common import *
from sense_finance.finance.model.base import *


class BaseReportData(BaseModel):
    class Meta:
        abstract = True

    def is_dim_yuan(self):
        return self.row_dim_type == ROW_DIM_YUAN

    def real_value(self, record):
        if not self.is_dim_yuan():
            return self.value
        rate = parse_float(record.report_rate)
        if rate <= 0:
            return self.value
        return self.value * record.report_rate


class ReportData(BaseReportData):
    id = models.AutoField(primary_key=True)
    report_record_id = models.IntegerField(blank=True, null=True)
    report_model_id = models.IntegerField(blank=True, null=True)
    row_dim_type = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_report_data')

    @property
    def record_key(self):
        return "s_{}".format(self.report_record_id)

    def data_type(self):
        return COMPANY_TYPE_SENSEDEAL


class CustomReportData(BaseModel):
    id = models.AutoField(primary_key=True)
    report_record_id = models.IntegerField(blank=True, null=True)
    report_model_id = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "CustomReportData(id={0},report_record_id={1},report_model_id={2},value={3}".format(self.id,
                                                                                                   self.report_record_id,
                                                                                                   self.report_model_id,
                                                                                                   self.value)

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_custom_report_data')

    def real_value(self, record):
        return self.value

    @property
    def record_key(self):
        return "c_{}".format(self.report_record_id)

    def data_type(self):
        return COMPANY_TYPE_CUSTOM


class CompanyTargetLatestData(BaseModel):
    id = models.AutoField(primary_key=True)
    report_scope = models.IntegerField(blank=True, null=True)
    report_model_id = models.IntegerField(blank=True, null=True)
    report_cycle = models.IntegerField(blank=True, null=True)
    report_period = models.IntegerField(blank=True, null=True)
    report_year = models.IntegerField(blank=True, null=True)
    company_code = models.CharField(max_length=100, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    first_industry_code = models.CharField(max_length=10, blank=True, null=True)
    second_industry_code = models.CharField(max_length=10, blank=True, null=True)
    three_industry_code = models.CharField(max_length=10, blank=True, null=True)
    four_industry_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_company_target_latest_data')

    def key(self):
        return self.get_key(self.company_code, self.report_scope, self.report_cycle, self.report_model_id)

    @classmethod
    def get_key(cls, company_code, report_scope, report_cycle, report_model_id):
        return "{0}_{1}_{2}_{3}".format(company_code, report_scope, report_cycle, report_model_id)

    def __str__(self):
        return "CompanyTargetLatestData(id={0},company_code={1},report_scope={2},report_cycle={7},report_model_id={3},report_year={4},report_period={5},value={6})".format(
            self.id, self.company_code, self.report_scope, self.report_model_id, self.report_year, self.report_period,
            self.value, self.report_cycle)
