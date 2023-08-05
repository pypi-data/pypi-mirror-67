from sense_finance.finance.common import FINANCE_DB, table_name
from sense_finance.finance.common import *
from sense_finance.finance.util import *
from sense_finance.finance.model.base import *


class IndustryTargetData(BaseModel):
    id = models.AutoField(primary_key=True)
    report_scope = models.IntegerField(blank=True, null=True)
    report_period = models.IntegerField(blank=True, null=True)
    report_year = models.IntegerField(blank=True, null=True)
    report_model_id = models.IntegerField(blank=True, null=True)
    target_type = models.IntegerField(blank=True, null=True)
    industry_id = models.CharField(max_length=200, blank=True, null=True)
    value = models.FloatField(blank=True, null=True, default=0)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_industry_target_data')

    def key(self):
        return "{0}_{1}_{2}_{3}_{4}_{5}".format(self.report_scope, self.report_period, self.report_year,
                                                self.report_model_id, self.target_type, self.industry_id)

    def get_time_key(self):
        return get_report_time_key(self.report_year, self.report_period)

    def get_report_cycle(self):
        return None

    def __str__(self):
        return "IndustryTargetData(report_scope={0},report_period={1},report_year={2},report_model_id={3},target_type={4},industry_id={5}) value={6}".format(
            self.report_scope, self.report_period, self.report_year, self.report_model_id, self.target_type,
            self.industry_id, self.value)
