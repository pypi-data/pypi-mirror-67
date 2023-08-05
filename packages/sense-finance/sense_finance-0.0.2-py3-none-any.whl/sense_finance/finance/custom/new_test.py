from sense_finance.finance.common import *
from sense_finance.finance.target.base import BaseTargetComputer
from sense_finance.finance.model import *
from sense_finance.finance.custom.new_parse import TargetExpressParser
from collections import defaultdict
from sense_finance.finance.custom.new_compute import NewCustomTargetComputer
from sense_finance.finance.helper.condition import TargetCondition


class NewCustomTargetTester(BaseTargetComputer):

    def _get_model_class(self, targets):
        model_class_map = defaultdict(int)
        name_set = set()
        for target in targets:
            if target.is_basic:
                model_class_map[target.model_class] += 1
                name_set.add(target.name)
        if not name_set:
            return ReportModel.objects.order_by('id').first().model_class
        for k, v in model_class_map.items():
            if v == len(name_set):
                return k
        sd.log_info("_get_model_class none for model_class_map={0} with name set={1}".format(model_class_map, name_set))
        return None

    def test_target(self, target):
        target.id = 0
        parser = TargetExpressParser(target.target_express, target.model_class)
        target_express_result = parser.parse()
        if not target_express_result:
            sd.log_info("test_target no target_express_result")
            return []
        limit = 60
        result_limit = 3
        company_codes = self._get_model_class_company_codes(target.model_class, limit)
        if not company_codes:
            sd.log_error("not found valid company_codes for {}".format(target))
            return []
        unit = 300
        size = int(len(company_codes) / unit)
        if size * unit < limit:
            size += 1
        sd.log_info("_get_model_class_company_codes size={0} size2={1}".format(len(company_codes), size))
        result = list()
        for i in range(size):
            end = (i + 1) * unit
            if end > len(company_codes):
                end = len(company_codes)
            ids = company_codes[i * unit:end]
            company_list = self.company_dao.gets_by_company_codes(ids)
            computer = NewCustomTargetComputer()
            condition = TargetCondition(report_time_type=REPORT_CYCLE_PERIOD, time_range_type=REPORT_TIME_RANGE_FIVE,
                                        combine_type=REPORT_BORE_COMBINE, compare_target=target,
                                        company=None, company_list=company_list,
                                        targets=target_express_result.get_targets())
            target_container = computer.compute(condition, target_express_result=target_express_result,
                                                test_limit=result_limit)
            items = self._build_test_result(condition, target, target_container, company_list,
                                            result_limit - len(result))
            sd.log_info(
                "_build_test_result size={0} for i={1} company_codes={2}".format(len(items), i, len(company_codes)))
            result.extend(items)
            if len(result) >= result_limit:
                return result
            if end > 2000:
                return result
        return result

    def _get_model_class_company_codes(self, model_class, limit):
        infos = list(CompanyInfo.objects.filter(model_class=model_class).all()[:limit])
        if len(infos) >= limit:
            return [info.company_code for info in infos]
        return [info.company_code for info in infos]

    def _build_test_result(self, condition, target, target_container, company_list, limit):
        result = list()
        company_map = {company.company_code: company for company in company_list}
        for company_code, company_data_map in target_container.company_data_map.items():
            val, data = company_data_map.get_latest_attr(target.field_key)
            if data is None:
                sd.log_info(
                    "_build_test_result data is none for {0},field_key={1}".format(company_code, target.field_key))
                continue
            time = get_show_report_time(condition.report_time_type, data.report_year,
                                        data.report_time_type)
            val = convert_target_normal_value(target, val, True)
            item = {
                'company_code': company_code,
                'company_name': company_map[company_code].company_full_name,
                'value': val,
                'time': time
            }
            result.append(item)
            if len(result) >= limit:
                break
        return result
