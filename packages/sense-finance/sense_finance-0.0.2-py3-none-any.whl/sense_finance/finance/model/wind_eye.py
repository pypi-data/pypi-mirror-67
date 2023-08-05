from sense_finance.finance.common import FINANCE_DB, table_name
from sense_finance.finance.common import *
from sense_finance.finance.util import *
from sense_finance.finance.model.base import *


class UserViewConfig(BaseModel):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=10, blank=True, null=True)
    company_code = models.CharField(max_length=50, blank=True, null=True)
    config = models.TextField(blank=True, null=True)
    view_type = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True,
                                       default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_user_view_config')

    def __str__(self):
        return "UserViewConfig(uid={0},view_type={1},company_code={2},config={3},update_time={4})".format(self.uid,
                                                                                                          self.view_type,
                                                                                                          self.company_code,
                                                                                                          self.config,
                                                                                                          self.update_time)

    @classmethod
    def find_config(cls, uid, view_type):
        uid = str(uid)
        item = cls.objects.filter(uid=uid, view_type=view_type).order_by('-id').first()
        if item:
            config = sd.load_json(item.config)
            if config:
                return config
        return cls.default_config(view_type)

    @classmethod
    @sd.try_catch_exception
    def save_config(cls, uid, view_type, config, company_code=''):
        item = cls.objects.filter(uid=uid, view_type=view_type).order_by('-id').first()
        if not item:
            item = cls()
            item.uid = uid
            item.view_type = view_type
        item.config = sd.dump_json(config)
        item.company_code = company_code
        item.update_time = datetime.datetime.now()
        item.save()
        sd.log_info("save config {}".format(item))

    @classmethod
    def default_config(cls, view_type):
        if view_type == VIEW_TYPE_COMPANY_REPORT:
            return {
                'report_time_type': REPORT_CYCLE_YEAR,
                'time_range_type': REPORT_TIME_RANGE_THREE,
                'combine_type': REPORT_BORE_COMBINE,
                'compare_type': COMPARE_MEAN_SIMPLE,
                'ratio_type': 0,
                'targets': ['营业利润', '营业收入', '资产总计'],
            }
        if view_type == VIEW_TYPE_INDUSTRY_REPORT:
            return {
                'report_time_type': REPORT_CYCLE_YEAR,
                'time_range_type': REPORT_TIME_RANGE_THREE,
                'limit_type': LIMIT_TYPE_TOP5,
                'compare_type': LIMIT_TYPE_TOP5,
                'compare_target': '营业收入',
                'ratio_type': 0,
                'targets': ['营业利润', '营业收入', '资产总计'],
            }
