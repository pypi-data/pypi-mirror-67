from sense_finance.finance.common import FINANCE_DB, table_name
from sense_finance.finance.common import *
from sense_finance.finance.util import *
from sense_finance.finance.model.base import *


class ReportModel(BaseModel):
    id = models.IntegerField(primary_key=True)
    model_class = models.CharField(max_length=3, blank=True, null=True)
    model_name = models.CharField(max_length=200, blank=True, null=True)
    model_no = models.IntegerField(blank=True, null=True)
    row_subject = models.CharField(max_length=32, blank=True, null=True)
    row_no = models.IntegerField(blank=True, null=True)
    report_name = models.CharField(max_length=200, blank=True, null=True)
    report_name_normal = models.CharField(max_length=200, blank=True, null=True)
    row_name = models.CharField(max_length=100, blank=True, null=True)
    row_name_normal = models.CharField(max_length=100, blank=True, null=True)
    row_name_sensedeal = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_report_model')

    def __str__(self):
        return "ReportModel(id={0},model_class={1},row_name={2},report_name={3}".format(self.id, self.model_class,
                                                                                        self.name, self.report_name)

    @property
    def name(self):
        if not self.row_name_normal:
            return ''
        return self.row_name_normal.strip()

    def show_report_name(self):
        return self.report_name_normal

    def is_valid_with(self, model):
        return self.model_class == model.model_class \
               and self.model_no == model.model_no \
               and self.row_subject == model.row_subject and self.row_no == model.row_no \
               and self.report_name == model.report_name \
               and self.row_name == model.row_name

    def is_same_with(self, model):
        return self.model_class == model.model_class and \
               self.model_name == model.model_name and self.model_no == model.model_no \
               and self.row_subject == model.row_subject and self.row_no == model.row_no \
               and self.report_name == model.report_name and self.report_name_normal == model.report_name_normal \
               and self.row_name == model.row_name and self.row_name_normal == model.row_name_normal \
               and self.row_name_sensedeal == model.row_name_sensedeal and self.unit == model.unit

    def param_name(self):
        return self.name
        # return "{0}:{1}".format(self.model_no, self.name)

    def is_unit_yuan(self):
        return self.unit == '元'

    def is_unit_day(self):
        return self.unit == '天' or self.unit == '天数'

    def is_unit_times(self):
        return self.unit == '次' or self.unit == '次数'

    def is_unit_percent(self):
        return self.unit == '%' or self.unit == '百分比'

    def is_valid(self):
        return self.report_name_normal and self.row_name_normal

    def need_update_industry(self):
        return True

    def get_update_industry_mean_types(self):
        return INDUSTRY_TARGET_TYPES

    def is_computing(self):
        return False

    @property
    def dim_type(self):
        if self.is_unit_yuan():
            return ROW_DIM_YUAN
        if self.is_unit_percent():
            return ROW_DIM_PERCENT
        if self.is_unit_times():
            return ROW_DIM_TIMES
        if self.is_unit_day():
            return ROW_DIM_DAY
        return ROW_DIM_NO

    @property
    def value(self):
        return self.id

    @property
    def is_basic(self):
        return True

    @property
    def is_custom(self):
        return False

    @property
    def field_key(self):
        return str(self.id)

    def is_using(self):
        return True

    def to_json(self, type=''):
        if type == 'config':
            result = {
                'id': self.id,
                'name': self.name
            }
        else:
            result = {
                'id': self.id,
                'name': self.name,
                'model_no': self.model_no,
                'report_name': self.report_name,
                'row_no': self.row_no,
            }
        return result


class CustomTarget(BaseModel):
    id = models.AutoField(primary_key=True)
    model_class = models.CharField(max_length=3, blank=True, null=True)
    model_name = models.CharField(max_length=200, blank=True, null=True)
    target_name = models.CharField(max_length=100)
    target_explain = models.TextField(blank=True, null=True)
    secret_level = models.IntegerField()
    target_express = models.TextField(blank=True, null=True)
    screen_user = models.TextField(blank=True, null=True)
    create_user = models.CharField(max_length=10, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True,
                                       default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    target_status = models.IntegerField()
    use_range = models.CharField(max_length=1000, blank=True, null=True)
    dim_type = models.IntegerField()

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_custom_target')

    def __str__(self):
        return "CustomTarget(id={0},target_name={1},target_express={2},create_user={3},target_status={4},dim_type={5}".format(
            self.id,
            self.target_name,
            self.target_express,
            self.create_user,
            self.target_status,
            self.dim_type)

    def need_update_industry(self):
        use_range = sd.load_json(self.use_range)
        if not use_range:
            return True
        industry = use_range.get('industry')
        return industry

    def get_update_industry_mean_types(self):
        use_range = sd.load_json(self.use_range)
        if not use_range:
            return INDUSTRY_TARGET_TYPES
        industry = use_range.get('industry')
        if not industry:
            return INDUSTRY_TARGET_TYPES
        return industry

    def need_update_report_time_type(self, report_time_type):
        use_range = sd.load_json(self.use_range)
        if not use_range:
            return True
        report_time_types = use_range.get('report_time_types')
        return report_time_type is None or report_time_type in report_time_types

    def show_report_name(self):
        if self.is_keep_target():
            return "财务指标表"
        return "自定义指标表"

    def is_unit_yuan(self):
        return self.dim_type == ROW_DIM_YUAN

    def is_unit_percent(self):
        return self.dim_type == ROW_DIM_PERCENT

    def is_unit_day(self):
        return self.dim_type == ROW_DIM_DAY

    def is_unit_times(self):
        return self.dim_type == ROW_DIM_TIMES

    def is_valid(self):
        return True

    def set_is_computing(self, flag):
        setattr(self, "computing0", flag)

    def is_computing(self):
        return getattr(self, "computing0", False)

    @property
    def status(self):
        return self.target_status

    @property
    def field_key(self):
        return str(self.id)

    @property
    def name(self):
        return self.target_name.strip()

    def param_name(self):
        return self.name

    def is_keep_target(self):
        return self.create_user == "00"

    def is_report_target(self):
        return self.is_keep_target() and self.target_name.find("_简报") > 0

    @property
    def is_basic(self):
        return False

    def is_using(self):
        return self.secret_level == TARGET_STATUS_PUBLIC and self.target_status == TARGET_STATUS_PUBLIC

    def is_status_public(self):
        return self.target_status == TARGET_STATUS_PUBLIC

    @property
    def is_custom(self):
        return True

    def to_json(self, type=''):
        if type == 'show':
            result = {
                'id': self.id,
                'target_name': self.target_name
            }
        else:
            desc = build_target_desc(self)
            result = {
                'id': self.id,
                'target_name': self.target_name,
                'dim_type': self.dim_type,
                'target_explain': self.target_explain,
                'secret_level': self.secret_level,
                'secret_level_value': convert_target_custom_secret_level(self.secret_level),
                'model_class': self.model_class,
                'model_name': self.model_name,
                'target_status': self.target_status,
                'target_desc': desc,
                'create_time': str(self.create_time)
            }
        return result


def get_basic_targets(targets):
    if not targets:
        return []
    return [target for target in targets if is_basic_target(target)]


def get_custom_targets(targets):
    if not targets:
        return []
    return [target for target in targets if is_custom_target(target) and target.id > 0]


def is_custom_target(target):
    return isinstance(target, CustomTarget)


def is_basic_target(target):
    return isinstance(target, ReportModel)


def is_custom_target_range(id):
    return id >= 999999


def convert_target_show_value(target, val):
    val2 = get_invalid_target_val(target, val)
    if val2 is not None:
        return 0
    val = parse_float(val)
    if target.is_unit_yuan():
        val = val * 1.0 / 10000
    if abs(val) >= 10000:
        return int(val)
    return round(val, 2)


def is_invalid_target_val(val):
    return val == INVALID_TARGET_DATA or val == COMPUTING_TARGET_DATA


def get_invalid_target_val(target, val):
    if val == INVALID_TARGET_DATA or val is None or val == COMPUTING_TARGET_DATA:
        if target.is_computing():
            return COMPUTING_TARGET_DATA
        return INVALID_TARGET_DATA
    return None


def convert_target_normal_value(target, val, use_unit=False):
    val2 = get_invalid_target_val(target, val)
    if val2 is not None:
        return val2
    val = parse_float(val)
    unit = ""
    if target.is_unit_percent():
        unit = "%"
    elif target.is_unit_yuan():
        val = val * 1.0 / 10000
        unit = "万元"
    elif target.is_unit_times():
        unit = "次"
    elif target.is_unit_day():
        unit = "天"
    val = "{:,.2f}".format(val)
    if val == '-0.00':
        val = '0.00'
    if not use_unit:
        return val
    return "{0}{1}".format(val, unit)


def show_target_name(target):
    if target.is_unit_yuan():
        return "{0}(万元)".format(target.name)
    if target.is_unit_percent():
        return "{0}(%)".format(target.name)
    if target.is_unit_times():
        return "{0}(次)".format(target.name)
    if target.is_unit_day():
        return "{0}(天)".format(target.name)
    return target.name


def refine_target_name(name):
    return parse_custom_target_format(name)


def filter_targets(targets):
    return [target for target in targets if target.is_valid()]


def build_target_desc(target):
    if target.is_basic:
        return ""
    return target.target_express or ""


class ModelClassSort(BaseModel):
    id = models.AutoField(primary_key=True)
    model_class = models.CharField(max_length=10, blank=True, null=True)
    sort_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('finance_model_class_sort')
