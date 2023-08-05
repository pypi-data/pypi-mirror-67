from sense_finance.finance.common import *
from sense_finance.finance.model import refine_target_name


class TargetNumItem(BasicConfigItem):

    def __init__(self, value, operator=None, depth=0):
        super(TargetNumItem, self).__init__(operator=operator, depth=depth)
        self.value = value

    def __str__(self):
        return "TargetNumItem(value={0},operator={1})".format(self.value, self.operator)

    def is_num(self):
        return True


class TargetItem(BasicConfigItem):

    def __init__(self, target_body, target_name, target_value, lost_type=None, convert_type=TARGET_VALUE_CONVERT_NO,
                 operator=None, depth=0):
        super(TargetItem, self).__init__(lost_type, convert_type, operator, depth)
        self.target_body = target_body
        self.target_name = refine_target_name(target_name)
        self.target_value = target_value

    def __str__(self):
        return "TargetItem(body={0},name={1},value={2},lost={3},convert={4},operator={5})".format(
            get_target_value_body_name(self.target_body),
            self.target_name,
            get_target_value_type_name(
                self.target_value),
            get_target_lost_type_name(self.lost_type),
            target_convert_type_name(
                self.convert_type),
            self.operator)

    def is_basic(self):
        return True

    def get_target_names(self):
        return [self.target_name]


def get_industry_target_type_map(items, target_map):
    result = dict()
    for item in items:
        target_type = get_industry_target_type(item.target_body)
        if not target_type:
            continue
        types = result.get(item.target_name)
        if not types:
            types = list()
        if target_type not in types:
            types.append(target_type)
        target = target_map.get(item.target_name)
        if not target:
            continue
        result[target.id] = types
    return result
