from sense_finance.finance.common import FINANCE_DB, table_name
from sense_finance.finance.util import *
from sense_finance.finance.model.base import *


class FinanceReportFactor(BaseModel):
    id = models.AutoField(primary_key=True)
    company_code = models.CharField(max_length=50)
    report_year = models.IntegerField()
    report_period = models.IntegerField()
    target_id = models.IntegerField()
    target_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_report_factor')

    @classmethod
    def find_factor(cls, report_year, report_period, company_code, target_id):
        return cls.objects.filter(report_year=report_year, report_period=report_period, company_code=company_code,
                                  target_id=target_id).first()

    @classmethod
    def build_new_factor(cls, report_year, report_period, company_code, target_id):
        factor = FinanceReportFactor(report_year=report_year, report_period=report_period,
                                     company_code=company_code, target_id=target_id)
        return factor

    @classmethod
    def update_or_create(cls, report_year, report_period, company_code, target_id, target_value):

        score = cls.find_factor(report_year, report_period, company_code, target_id)
        if not score:
            score = cls.build_new_factor(report_year, report_period, company_code, target_id)
            score.save()
            sd.log_info('save FinanceReportFactor, report_year={0}, report_period={1}, '
                        'company_code={2}, target_id={3}, target_value={4}'.format(report_year, report_period,
                                                                                   company_code, target_id,
                                                                                   target_value))
            return 1

        if score.target_value != target_value:
            score.target_value = target_value
            score.save()
            sd.log_info('update FinanceReportFactor, report_year={0}, report_period={1}, '
                        'company_code={2}, target_id={3}, target_value={4}'.format(report_year, report_period,
                                                                                   company_code, target_id,
                                                                                   target_value))
            return 2
        return 0

    def to_json(self, type=''):
        result = {
            'company_code': self.company_code,
            'report_year': self.report_year,
            'report_period': self.report_period,
            'target_id': self.target_id,
            'target_value': self.target_value
        }
        return result


class FinanceReportScore(BaseModel):
    id = models.AutoField(primary_key=True)
    company_code = models.CharField(max_length=50)
    report_year = models.IntegerField()
    report_period = models.IntegerField()
    target_id = models.IntegerField()
    target_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_report_score')

    @classmethod
    def find_report_score(cls, report_year, report_period, company_code, target_id):
        return cls.objects.filter(report_year=report_year, report_period=report_period, company_code=company_code,
                                  target_id=target_id).first()

    @classmethod
    def build_new_score(cls, report_year, report_period, company_code, target_id, target_value):
        score = FinanceReportScore(report_year=report_year, report_period=report_period,
                                   company_code=company_code, target_id=target_id, target_value=target_value)
        return score

    @classmethod
    def update_or_create(cls, report_year, report_period, company_code, target_id, target_value):
        sd.log_info('update_or_create FinanceReportScore, report_year={0}, report_period={1}, '
                    'company_code={2}, target_id={3}, target_value={4}'.format(report_year, report_period,
                                                                               company_code, target_id,
                                                                               target_value))
        score = cls.find_report_score(report_year, report_period, company_code, target_id)
        if not score:
            score = cls.build_new_score(report_year, report_period, company_code, target_id, target_value)
            score.save()
        elif score.target_value == target_value:
            return
        elif score.target_value != target_value:
            score.target_value = target_value
            score.save()

    @classmethod
    def get_current_period(cls, company_code):
        item = cls.objects.filter(company_code=company_code).order_by('-report_year', '-report_period').first()
        if not item:
            return None, None
        return item.report_year, item.report_period

    def to_json(self, type=''):
        result = {
            'company_code': self.company_code,
            'report_year': self.report_year,
            'report_period': self.report_period,
            'target_id': self.target_id,
            'target_value': self.target_value
        }
        return result


class FinanceReportFinalScore(BaseModel):
    id = models.AutoField(primary_key=True)
    company_code = models.CharField(max_length=50)
    company_name = models.CharField(max_length=200)
    report_year = models.IntegerField(blank=True, null=True)
    report_period = models.IntegerField(blank=True, null=True)
    report_score = models.FloatField(blank=True, null=True)
    report_level = models.IntegerField(blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    grow = models.FloatField(blank=True, null=True)
    cash_flow = models.FloatField(blank=True, null=True)
    operate = models.FloatField(blank=True, null=True)
    debt = models.FloatField(blank=True, null=True)
    profit_level = models.IntegerField(blank=True, null=True)
    grow_level = models.IntegerField(blank=True, null=True)
    cash_flow_level = models.IntegerField(blank=True, null=True)
    operate_level = models.IntegerField(blank=True, null=True)
    debt_level = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_report_final_score')

    @classmethod
    def find_report_score(cls, report_year, report_period, company_code):
        return cls.objects.filter(report_year=report_year, report_period=report_period,
                                  company_code=company_code).first()

    @classmethod
    def build_new_score(cls, report_year, report_period, company_code):
        score = FinanceReportFinalScore(report_year=report_year, report_period=report_period, company_code=company_code)
        return score

    @classmethod
    def update_or_create(cls, report_year, report_period, company_code, company_name, report_score, report_level,
                         five_dims_score):
        sd.log_info('update_or_create FinanceReportFinalScore, report_year={0}, report_period={1}, company_code={2},'
                    ' report_score={3}'.format(report_year, report_period, company_code, report_score))
        score = cls.find_report_score(report_year, report_period, company_code)
        if not score:
            score = cls.build_new_score(report_year, report_period, company_code)
        score.company_name = company_name
        score.report_score = report_score
        score.report_level = report_level
        score.update_time = datetime.datetime.now()
        for dim, value in five_dims_score.items():
            key = cls._get_five_dims_name(dim)
            if key:
                setattr(score, key, value)
        score.save()

    def to_res(self, company_dict=None):
        if not company_dict:
            result = {
                'company_code': self.company_code,
                'company_name': self.company_name,
                'report_score': self.report_score if self.report_score else '-',
                'score_time': self.update_time.strftime("%Y-%m-%d %H:%M:%S"),
                'report_level': self._convert_report_level(self.report_level),
                'current_level': '',
                'last_level': '',
                'update_time': ''
            }
            return result
        else:
            company = company_dict.get(self.company_name)
            if not company:
                return None
            result = {
                'company_code': self.company_code,
                'company_name': self.company_name,
                'report_score': self.report_score if self.report_score else '-',
                'score_time': self.update_time.strftime("%Y-%m-%d %H:%M:%S"),
                'report_level': self._convert_report_level(self.report_level),
                'current_level': company['current_level'],
                'last_level': company['last_level'],
                'update_time': company['update_time']
            }
            return result

    def _convert_report_level(self, report_level):
        if report_level == 1:
            return '低'
        elif report_level == -1:
            return '高'
        return '中'

    @classmethod
    def _get_five_dims_name(self, key):
        if key == '盈利能力':
            return 'profit'
        elif key == '成长能力':
            return 'grow'
        elif key == '现金流量':
            return 'cash_flow'
        elif key == '运营能力':
            return 'operate'
        elif key == '偿债能力':
            return 'debt'
        elif key == 'profit_level':
            return 'profit_level'
        elif key == 'grow_level':
            return 'grow_level'
        elif key == 'cash_flow_level':
            return 'cash_flow_level'
        elif key == 'operate_level':
            return 'operate_level'
        elif key == 'debt_level':
            return 'debt_level'
        return None

    def to_json(self, type=''):
        result = {
            'company_code': self.company_code,
            'report_year': self.report_year,
            'report_period': self.report_period,
            'profit_level': self.profit_level,
            'grow_level': self.grow_level,
            'cash_flow_level': self.cash_flow_level,
            'operate_level': self.operate_level,
            'debt_level': self.debt_level,
        }
        return result


class RiskReportScore(BaseModel):
    id = models.AutoField(primary_key=True)
    company_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    report_year = models.IntegerField(blank=True, null=True)
    report_period = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_risk_report_score')
