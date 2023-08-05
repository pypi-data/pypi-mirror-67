from sense_finance.finance.common import FINANCE_DB, table_name
from sense_finance.finance.model.base import *
from sense_finance.finance.common import *
import sense_core as sd


class CompanyModelClass(BaseModel):
    id = models.CharField(primary_key=True)
    model_class = models.CharField(max_length=50)
    industry_id = models.CharField(max_length=50)
    industry_name = models.CharField(max_length=50)
    parent_industry_id = models.CharField(max_length=50)
    parent_industry_name = models.CharField(max_length=50)
    update_time = models.BigIntegerField()

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_company_model_class')

    def __str__(self):
        return "CompanyModelClass(id={0},model_class={1},industry_id={2},industry_name={3},parent_industry_id={4},parent_industry_name={5}".format(
            self.id, self.model_class, self.industry_id, self.industry_name, self.parent_industry_id,
            self.parent_industry_name)


class IndustryReportUpdateInfo(BaseModel):
    id = models.IntegerField(primary_key=True)
    last_id = models.IntegerField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_industry_report_update_info')

    def __str__(self):
        return "IndustryReportUpdateInfo(id={0},last_id={1},update_time={2}".format(self.id,
                                                                                    self.last_id,
                                                                                    self.update_time)

