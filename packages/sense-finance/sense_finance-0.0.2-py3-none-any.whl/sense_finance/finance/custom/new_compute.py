from sense_finance.finance.target.base import BaseTargetComputer
from sense_finance.finance.model import *
from sense_finance.finance.common import *
from sense_finance.finance.custom.new_parse import TargetExpressParser
from sense_finance.finance.custom.compute_value import CustomTargetValueComputer


class NewCustomTargetComputer(BaseTargetComputer):

    def __init__(self):
        super(NewCustomTargetComputer, self).__init__()

    def _build_express_result(self, condition):
        target_express = condition.compare_target.target_express
        if not target_express:
            sd.log_error("not found target_express for {0} target={1}".format(condition, condition.compare_target.id))
            return None
        parser = TargetExpressParser(target_express, condition.model_class)
        result = parser.parse()
        return result

    def compute(self, condition, need_none=False, target_container=None, industry_container=None,
                target_express_result=None, test_limit=0):
        if not target_express_result:
            target_express_result = self._build_express_result(condition)
        if not target_express_result:
            sd.log_error(
                "no target_express_result for condition={} target={}".format(condition, condition.compare_target))
            return None
        condition.targets = target_express_result.get_targets()
        return self.compute0(condition, target_express_result, need_none, target_container, industry_container,
                             test_limit)

    def compute0(self, condition, target_express_result, need_none=False, target_container=None,
                 industry_container=None, test_limit=0):
        time_types = get_custom_report_time_types(condition.report_time_type)
        target = condition.compare_target
        if not target_container:
            target_container = self.target_data_dao.select_target_result(condition)
        self.target_container = target_container
        if condition.report_record:
            computer = CustomTargetValueComputer(condition, target, target_container, industry_container,
                                                 target_express_result,
                                                 condition.report_record.report_year,
                                                 condition.report_record.report_period)
            val = computer.compute_value(False)
            if sd.is_debug():
                sd.log_info("compute_value got {0} for report_record={1}".format(val, condition.report_record.id))
            return val
        if test_limit > 0:
            test_size = 0
            for year in range(condition.end_year, condition.start_year - 1, -1):
                for time_type in time_types:
                    computer = CustomTargetValueComputer(condition, target, target_container, industry_container,
                                                         target_express_result, year,
                                                         time_type, need_none)
                    compute_size = computer.compute_value(True)
                    if compute_size:
                        test_size += compute_size
                    if test_size >= test_limit:
                        return target_container
            return target_container
        for year in range(condition.start_year, condition.end_year + 1):
            for time_type in time_types:
                computer = CustomTargetValueComputer(condition, target, target_container, industry_container,
                                                     target_express_result, year,
                                                     time_type, need_none)
                computer.compute_value()
        return target_container
