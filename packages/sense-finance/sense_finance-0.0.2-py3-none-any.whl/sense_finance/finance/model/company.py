from sense_finance.finance.common import *
from sense_finance.finance.util import *
from sense_finance.finance.model.base import *


class CompanyInfo(BaseModel):
    id = models.AutoField(primary_key=True)
    stock_code = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_code = models.CharField(max_length=50, blank=True, null=True)
    company_full_name = models.CharField(max_length=100, blank=True, null=True)
    first_industry_code = models.CharField(max_length=10, blank=True, null=True)
    first_industry_name = models.CharField(max_length=50, blank=True, null=True)
    second_industry_code = models.CharField(max_length=10, blank=True, null=True)
    second_industry_name = models.CharField(max_length=50, blank=True, null=True)
    three_industry_code = models.CharField(max_length=10, blank=True, null=True)
    three_industry_name = models.CharField(max_length=50, blank=True, null=True)
    four_industry_code = models.CharField(max_length=10, blank=True, null=True)
    four_industry_name = models.CharField(max_length=50, blank=True, null=True)
    model_class = models.CharField(max_length=50, blank=True, null=True)
    social_credit_code = models.CharField(max_length=100, blank=True, null=True)
    organization_code = models.CharField(max_length=100, blank=True, null=True)
    business_license = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        app_label = FINANCE_DB
        db_table = table_name('company_info')

    @classmethod
    def find_with_model_class(cls):
        return cls.objects.filter(model_class__isnull=False).all()

    def is_sensedeal(self):
        return True

    @property
    def is_stock(self):
        return getattr(self, 'stock_flag', True)

    @is_stock.setter
    def is_stock(self, flag):
        setattr(self, 'stock_flag', flag)

    def has_industry(self):
        return self.first_industry_code

    def industry_ids(self):
        items = list()
        if self.first_industry_code:
            items.append(self.first_industry_code.strip())
        if self.second_industry_code:
            items.append(self.second_industry_code.strip())
        if self.three_industry_code:
            items.append(self.three_industry_code.strip())
        if self.four_industry_code:
            items.append(self.four_industry_code.strip())
        return items

    def is_in_industry_ids(self, industry_ids):
        if self.second_industry_code and self.second_industry_code in industry_ids:
            return True
        if self.three_industry_code and self.three_industry_code in industry_ids:
            return True
        if self.four_industry_code and self.four_industry_code in industry_ids:
            return True
        if self.first_industry_code and self.first_industry_code in industry_ids:
            return True
        return False

    @property
    def parent_industry_name(self):
        return self.first_industry_name.strip() if self.first_industry_name else ""

    @property
    def industry_name(self):
        return self.second_industry_name.strip() if self.second_industry_name else ""

    @property
    def industry_id(self):
        if self.four_industry_code:
            return self.four_industry_code
        if self.three_industry_code:
            return self.three_industry_code
        return self.second_industry_code.strip() if self.second_industry_code else ""

    @property
    def parent_industry_id(self):
        return self.first_industry_code.strip() if self.first_industry_code else ""

    def get_industry_name(self, industry_id):
        if self.four_industry_code == industry_id:
            return self.four_industry_name
        if self.three_industry_code == industry_id:
            return self.three_industry_name
        if self.second_industry_code == industry_id:
            return self.second_industry_name
        if self.first_industry_code == industry_id:
            return self.first_industry_name
        return ''

    def to_json(self, type=''):
        result = {
            'id': self.id,
            'company_name': self.company_full_name,
            'company_code': self.company_code,
            'pin_yin': chinese_to_pinyin_str(self.company_full_name),
            'first_industry_code': self.first_industry_code.strip() if self.first_industry_code else self.first_industry_code,
            'first_industry_name': self.first_industry_name.strip() if self.first_industry_name else self.first_industry_name,
            'first_industry_pin_yin': chinese_to_pinyin_str(self.first_industry_name),
            'second_industry_code': self.second_industry_code.strip() if self.second_industry_code else self.second_industry_code,
            'second_industry_name': self.second_industry_name.strip() if self.second_industry_name else self.second_industry_name,
            'second_industry_pin_yin': chinese_to_pinyin_str(self.second_industry_name),
            'three_industry_code': self.three_industry_code.strip() if self.three_industry_code else self.three_industry_code,
            'three_industry_name': self.three_industry_name.strip() if self.three_industry_name else self.three_industry_name,
            'three_industry_pin_yin': chinese_to_pinyin_str(self.three_industry_name),
            'four_industry_code': self.four_industry_code.strip() if self.four_industry_code else self.four_industry_code,
            'four_industry_name': self.four_industry_name.strip() if self.four_industry_name else self.four_industry_name,
            'four_industry_pin_yin': chinese_to_pinyin_str(self.four_industry_name),
            'is_stock': 1 if self.is_stock else 0
        }
        if self.has_industry():
            result['in_industry'] = 1
        else:
            result['in_industry'] = 0
        return result

    def to_industry_json(self, type=''):
        if type == 'company':
            result = {
                'company_name': self.company_full_name,
                'pin_yin': chinese_to_pinyin_str(self.company_full_name),
            }
        else:
            result = {
                'company_name': self.company_full_name,
                'pin_yin': chinese_to_pinyin_str(self.company_full_name),
                'first_industry_code': self.first_industry_code.strip() if self.first_industry_code else self.first_industry_code,
                'second_industry_code': self.second_industry_code.strip() if self.second_industry_code else self.second_industry_code,
                'three_industry_code': self.three_industry_code.strip() if self.three_industry_code else self.three_industry_code,
                'four_industry_code': self.four_industry_code.strip() if self.four_industry_code else self.four_industry_code,
            }
        return result

    def __str__(self):
        return "{}".format(self.to_json())
