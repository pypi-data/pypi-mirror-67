from collections import defaultdict
import sense_core as sd
from sense_finance.finance.common import *
from sense_finance.finance.helper.common import *


class ComputeTargetItem(object):

    def __init__(self, report_time_type, year, time_type, target_body, target_name, target_value):
        self.report_time_type = report_time_type
        self.year = year
        self.time_type = time_type
        self.target_body = target_body
        self.target_name = target_name
        self.target_value = target_value


class SingleTargetItem(object):

    def __init__(self, company, value):
        self.company = company
        self.value = value

    @property
    def company_id(self):
        return self.company.company_code


class SingleIndustryTargetDataMap(object):

    def __init__(self):
        self.target_map = defaultdict(list)

    def add(self, model_id, item):
        self.target_map[model_id].append(item)

    def get(self, model_id):
        return self.target_map.get(model_id)


class IndustryTargetDataMap(object):

    def __init__(self):
        self.target_map = defaultdict(dict)

    def add(self, model_id, item):
        items = self.target_map[model_id].get(item.get_time_key())
        if not items:
            items = list()
            self.target_map[model_id][item.get_time_key()] = items
        items.append(item)

    def get_item(self, model_id, time_key):
        map = self.target_map.get(model_id)
        if not map:
            return None
        items = map.get(time_key)
        return items[0] if items else None

    def get_map(self, model_id):
        return self.target_map.get(model_id)

    def __len__(self):
        return len(self.target_map)

    def debug(self):
        for model, _map in self.target_map.items():
            sd.log_info("model_id:{}".format(model))
            for k, v in _map.items():
                sd.log_info("time_key={0},value={1}".format(k, v[0].value))


class TargetCompareContainer(object):

    def __init__(self):
        self.time_weight_map = defaultdict(dict)

    def add(self, key, company_id, val):
        self.time_weight_map[key][company_id] = val

    def get(self, key):
        return self.time_weight_map.get(key)

    def recompute(self):
        for _, map in self.time_weight_map.items():
            total = 0
            for v in map.values():
                total += v
            for k in map.keys():
                map[k] = round(map[k] * 1.0 / total, 8)
        sd.log_info("_build_company_weight_map={}".format(self.time_weight_map))


class TargetData(object):

    def __init__(self, report_year, report_month, report_time_type, company_id, combine_type=None,
                 report_record=None):
        self.report_time_type = report_time_type
        self.report_year = report_year
        self.report_month = report_month
        self.company_id = company_id
        self.combine_type = combine_type
        self.report_record = report_record
        self.attrs = dict()

    def __repr__(self):
        return "TargetData(time_type={0},year={1},report_month={4},company={2},record_id={5},attr={3})".format(
            self.report_time_type,
            self.report_year,
            self.company_id,
            self.attrs,
            self.report_month, self.report_record_id)

    @property
    def report_record_id(self):
        return self.report_record.id

    @property
    def time_key(self):
        return get_report_time_key(self.report_year, self.report_time_type)

    def add_attr(self, key, val):
        self.attrs[str(key)] = val

    def get_attr(self, key, default_value=None):
        val = self.attrs.get(str(key))
        if val is None:
            return default_value
        return val

    def get_target_attr(self, targets):
        if type(targets) != list:
            return self.get_attr(targets.field_key)
        for target in targets:
            val = self.get_attr(target.field_key)
            if val is not None:
                return val
        return None

    def is_latest_than(self, data):
        return TargetData.cmp_data(self, data) > 0

    @classmethod
    def cmp_data(cls, data1, data2):
        if data1.report_year < data2.report_year:
            return -1
        if data1.report_year > data2.report_year:
            return 1
        if get_report_month(data1.report_time_type) > get_report_month(data2.report_time_type):
            return 1
        return -1


class CompanyTargetData(object):

    def __init__(self):
        self.items = list()
        self.time_map = dict()

    def __repr__(self):
        return "CompanyTargetData({})".format(self.items)

    def append(self, data):
        self.items.append(data)
        self.time_map[data.time_key] = data

    def get_latest_data(self):
        latest = None
        for item in self.items:
            if not latest:
                latest = item
            elif item.is_latest_than(latest):
                latest = item
        return latest

    def get_latest_attr_data(self):
        latest = None
        for item in self.items:
            if not latest:
                latest = item
            elif item.is_latest_than(latest):
                latest = item
        return latest

    def get_latest_attr(self, name):
        latest = None
        for i, item in enumerate(self.items):
            val = item.get_attr(name)
            if val is None:
                continue
            if not latest:
                latest = item
            elif item.is_latest_than(latest):
                latest = item
        if not latest:
            return None, None
        return latest.get_attr(name), latest

    def get(self, key):
        return self.time_map.get(key)


class TargetDataContainer(object):

    def __init__(self, company_data_map=None,record_items=None):
        self.company_data_map = company_data_map
        self.time_data_map = defaultdict(list)
        self.data_list = list()
        self.record_items = record_items
        self.time_company_data_map = dict()
        self.add_company_data_map(company_data_map)

    def add_company_data_map(self, company_data_map):
        for company_data in company_data_map.values():
            for k, v in company_data.time_map.items():
                self.data_list.append(v)
                self.time_data_map[k].append(v)
                self.time_company_data_map[k + "_" + v.company_id] = v

    def time_data_items(self, key):
        return self.time_data_map.get(key)

    def company_keys(self):
        return self.company_data_map.keys()

    def get_sort_data_list(self):
        return sorted(self.data_list, key=lambda x: (x.report_year, x.report_month), reverse=True)

    def has_time_data_items(self, key):
        return key in self.time_data_map

    def get_target_field_key_set(self):
        key_set = set()
        for data in self.data_list:
            key_set.update(data.attrs.keys())
        return key_set

    def time_company_item(self, key, company_id):
        return self.time_company_data_map.get(key + "_" + company_id)

    def __repr__(self):
        return "TargetDataContainer(company_data_map={})".format(self.company_data_map)


class CompanyIndustryTargetData(object):

    def __init__(self):
        self.items = list()
        self.time_map = defaultdict(list)

    def __repr__(self):
        return "CompanyTargetData({})".format(self.items)

    def append(self, data):
        self.items.append(data)
        self.time_map[data.time_key].append(data)

    def get(self, key):
        return self.time_map.get(key)

    def get_industry_id(self, key, industry_id):
        items = self.time_map.get(key)
        if not items:
            return None
        for item in items:
            if item.industry_id == industry_id:
                return item
        return None


class IndustryTargetDataContainer(object):

    def __init__(self):
        self.data_map = dict()

    def extend(self, items):
        for item in items:
            self.data_map[item.key()] = item

    def get_value(self, item):
        item2 = self.data_map.get(item.key())
        return item2.value if item2 else None
