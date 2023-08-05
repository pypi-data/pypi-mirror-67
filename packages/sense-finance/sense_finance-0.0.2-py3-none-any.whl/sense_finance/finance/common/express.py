from .constants import *
import sense_core as sd


class BasicConfigItem(object):
    def __init__(self, lost_type=None, convert_type=TARGET_VALUE_CONVERT_NO,
                 operator=None, depth=0):
        self.lost_type = lost_type
        self.convert_type = convert_type
        self.operator = operator
        self.depth = depth

    def get_depth_tab(self):
        if self.depth == 0:
            return ""
        return "".join(["  " for i in range(self.depth)])

    def is_basic(self):
        return False

    def is_composite(self):
        return False

    def is_num(self):
        return False


class CompositeExpress(BasicConfigItem):

    def __init__(self, operator=None, lost_type=None, convert_type=TARGET_VALUE_CONVERT_NO, depth=1):
        super(CompositeExpress, self).__init__(lost_type, convert_type, operator, depth)
        self.items = list()

    def __str__(self):
        desc = ""
        for item in self.items:
            desc += "\n{0}{1}".format(self.get_depth_tab(), item)
        return "CompositeExpress(operator={0},lost={1},convert={2},items={3})".format(self.operator,
                                                                                      get_target_lost_type_name(
                                                                                          self.lost_type),
                                                                                      target_convert_type_name(
                                                                                          self.convert_type), desc)

    def is_composite(self):
        return True

    def add(self, item):
        self.items.append(item)
        # sd.log_info("add {0}".format(item))

    def __len__(self):
        return len(self.items)

    def get_all_basic_items0(self, names):
        for item in self.items:
            if item.is_basic():
                names.append(item)
                continue
            if item.is_composite():
                item.get_all_basic_items0(names)
        return names

    def get_all_basic_items(self):
        return self.get_all_basic_items0(list())

    def get_all_target_names(self, items=None):
        if not items:
            items = self.get_all_basic_items()
        return self._build_target_names(items)

    def _build_target_names(self, items):
        result = set()
        for item in items:
            result.update(item.get_target_names())
        return result

    def get_all_company_target_names(self, items=None):
        if not items:
            items = self.get_all_basic_items()
        if not items:
            return set()
        if not hasattr(items[0], 'target_body'):
            return self._build_target_names(items)
        return self._build_target_names([item for item in items if item.target_body == TARGET_BODY_COMPANY])


class ExpressResult(object):

    def __init__(self, express, target_map, company_target_map, model_class):
        self.express = express
        self.target_map = target_map
        self.company_target_map = company_target_map
        self.model_class = model_class

    def get_targets(self):
        return list(self.target_map.values())

    def get_company_targets(self):
        return list(self.company_target_map.values())

    def get_target(self, name):
        return self.target_map.get(name)

    def __str__(self):
        return "ExpressResult(express={0},model_class={1},target_map={2},company_target_map={3})".format(self.express,
                                                                                                         self.model_class,
                                                                                                         len(
                                                                                                             self.target_map),
                                                                                                         len(
                                                                                                             self.company_target_map))
