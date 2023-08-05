from sense_finance.finance.dao import TargetDAO
from sense_finance.finance.common import *


class BaseExpressParser(object):

    def __init__(self, text, model_class):
        self.error = None
        self.text = text
        self.model_class = model_class
        self.target_dao = TargetDAO()

    def is_nest_item(self, item):
        return type(item) == list

    def validate(self):
        self.parse()
        return self.error

    def parse_express(self):
        pass

    def parse_basic_items(self):
        result = self.parse()
        if not result:
            return None
        return result.express.get_all_basic_items()

    def parse(self):
        if not self.text:
            self.error = "公式不能为空"
            return None
        items = self.parse_express()
        if not items:
            return None
        express = self.convert_result(items, CompositeExpress())
        if not express:
            self.error = "公式转换失败"
            return None
        return self.build_result(express)

    def convert_result(self, items, result):
        pass

    def build_result(self, express):
        items = express.get_all_basic_items()
        target_names = express.get_all_target_names(items)
        company_target_names = express.get_all_company_target_names(items)
        if not target_names:
            self.error = "没有有效的指标项"
            return None
        targets = self.target_dao.find_targets_by_names(target_names, self.model_class)
        target_map = {target.name: target for target in targets}
        company_target_map = dict()
        for target_name in target_names:
            target = target_map.get(target_name)
            if not target:
                self.error = "指标项 \"{0}\" 无效".format(target_name)
                return None
            if target_name in company_target_names:
                company_target_map[target_name] = target
        result = ExpressResult(express, target_map, company_target_map, self.model_class)
        return result
