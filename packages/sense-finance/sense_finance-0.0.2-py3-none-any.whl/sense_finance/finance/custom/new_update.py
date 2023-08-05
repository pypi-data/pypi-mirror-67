from sense_finance.finance.dao import *
from sense_finance.finance.target.base_update import BaseTargetUpdater
from sense_finance.finance.custom.new_compute import NewCustomTargetComputer
from sense_finance.finance.helper.condition import TargetCondition
from sense_finance.finance.custom.new_parse import TargetExpressParser
from sense_finance.finance.custom.core import get_industry_target_type_map


class NewCustomTargetUpdater(BaseTargetUpdater):

    def __init__(self):
        super(NewCustomTargetUpdater, self).__init__()
        self.target_express_result_map = dict()
        self.industry_data_container = None

    @sd.try_catch_exception
    def clear_data(self):
        del self.target_map
        del self.record_map
        del self.target_express_result_map
        del self.company_record_map
        del self.company_data_map

    @sd.try_catch_exception
    def update_record(self, record, target=None):
        sd.TimeCost.reset_time()
        if not target:
            targets = self.target_dao.find_public_custom_targets(record.model_class)
            sd.log_info("get custom target size={0} model_class={1}".format(len(targets), record.model_class))
        else:
            targets = [target]
        if not targets:
            return
        custom_record = self.report_data_dao.make_sure_custom_record(record)
        if sd.is_debug():
            sd.log_info("make_sure_custom_record custom_record {}".format(custom_record))
        if not custom_record:
            sd.log_error("make_sure_custom_record not found custom_record for {}".format(record))
            return
        data_items = self.report_data_dao.find_by_record_model([record, custom_record], targets)
        data_map = {data.report_model_id: data for data in data_items}
        for target in targets:
            self.update_record_target(custom_record, record, target, data_map.get(target.id))
        sd.log_info("done update_custom_target record={0} cost={1}".format(record.id, sd.TimeCost.show_time_diff()))

    @sd.try_catch_exception
    def update_all(self, thread_num=1, mod_index=1, mod_size=1):
        start_time = sd.get_current_second()
        target_dao = TargetDAO()
        targets = target_dao.find_public_custom_targets()
        sd.log_info("get custom_targets size = {}".format(len(targets)))
        if mod_size > 1:
            targets = [target for target in targets if target.id % mod_size == mod_index]
        sd.log_info(
            "update_all custom_targets real size = {0} mod_index={1} mod_size={2}".format(len(targets), mod_index,
                                                                                          mod_size))
        self.load_model_class_company_map()
        self.load_record_map()
        for target in targets:
            self.update_target(target, thread_num)
        sd.log_info(
            "done update_all targets = {0} cost={1} mod_index={2} mod_size={3}".format(len(targets), (
                    sd.get_current_second() - start_time), mod_index, mod_size))
        self.clear_data()

    def get_target_express_result(self, target):
        target_express_result = self.target_express_result_map.get(target)
        if target_express_result:
            return target_express_result
        if not target.target_express:
            return None
        parser = TargetExpressParser(target.target_express, target.model_class)
        target_express_result = parser.parse()
        if not target_express_result:
            sd.log_error("get_target_express_result not parse well for {}".format(target))
            return None
        sd.log_info("get_target_express_result result = {}".format(target_express_result))
        self.target_map[target] = target_express_result.get_targets()
        self.target_express_result_map[target] = target_express_result
        return target_express_result

    # 一个对象只能调用一次该方法，确保recrods是争取的
    @sd.try_catch_exception
    def update_target(self, target, thread_num=4):
        start_time = sd.get_current_second()
        sd.log_info(
            "start update_custom_target={0} model_class={1} id={2}".format(target.name, target.model_class, target.id))
        self.same_count = 0
        self.update_count = 0
        self.new_count = 0
        self.delete_count = 0
        self.old_count = 0
        close_model_connection()
        express_result = self.get_target_express_result(target)
        if not express_result:
            sd.log_error("not found target_express_result for target={}".format(target))
            return True
        targets = self.target_map[target]
        targets2 = list(targets)
        targets2.append(target)
        models = self.get_target_record_models(targets2)
        sd.log_info("update_target get_target_record_models={0} for {1}".format(models, target.id))
        self.load_record_map(target, models)
        company_targets = express_result.get_company_targets()
        if company_targets:
            self.load_targets_data(company_targets)
        self.old_count = self.load_targets_data([target], False)
        self.industry_data_container = self.load_industry_data_container(express_result)
        companys = self.load_model_class_company_map(target.model_class)
        sd.log_info(
            "load_model_class_company_map size={0} for model_class={1}".format(len(companys), target.model_class))
        items = [{
            'target': target,
            'company': company,
        } for company in companys]
        start_time1 = sd.get_current_second()
        sd.execute_multi_core('update_target', self._update_thread_target, items, thread_num, True)
        sd.log_info(
            "done update_custom_target={0} model_class={1} cost={2} id={3}  old={4} new={5} update={6} delete={7} total={8} upate_time={9}".format(
                target.name, target.model_class,
                (sd.get_current_second() - start_time),
                target.id, self.old_count, self.new_count, self.update_count, self.delete_count, len(companys),
                (sd.get_current_second() - start_time1)))
        return True

    def load_industry_data_container(self, express_result):
        items = express_result.express.get_all_basic_items()
        target_type_map = get_industry_target_type_map(items, express_result.target_map)
        if not target_type_map:
            return None
        return self.industry_data_dao.load_industry_data_container(target_type_map)

    def _update_thread_target(self, item):
        self.update_company_target(item['target'], item['company'])

    @sd.try_catch_exception
    def update_company_target(self, target, company):
        sd.log_info(
            "start update_company_target target={0} company={1}".format(target.id, company.company_code))
        record_items = self.company_record_map.get(company.company_code)
        data_items = self.company_data_map.get(company.company_code)
        size = self._update_company_target0(target, company, record_items, data_items)
        sd.log_info(
            "end update_company_target target={0} size={1} company={2}".format(target.id, size, company.company_code))

    def _update_company_target0(self, target, company, record_items, data_items):
        if not record_items:
            return 0
        if not data_items:
            return 0
        custom_record_map = self.load_company_custom_records(company.company_code, record_items)
        cycle_types = get_custom_report_cycle_types()
        combine_types = get_combine_types()
        target_express_result = self.get_target_express_result(target)
        if not target_express_result:
            return 0
        data_list_result = list()
        for cycle_type in cycle_types:
            if company.is_sensedeal() and not target.need_update_report_time_type(cycle_type):
                continue
            for combine_type in combine_types:
                target_container = self.target_data_dao.build_target_container(record_items, data_items, cycle_type,
                                                                               combine_type)
                if not target_container:
                    continue
                condition = TargetCondition(report_time_type=cycle_type, combine_type=combine_type,
                                            report_time_types=get_custom_report_time_types(cycle_type),
                                            compare_target=target, company_list=[company],
                                            model_class=target.model_class, time_range_type=REPORT_TIME_RANGE_SIX,
                                            targets=target_express_result.get_targets())
                computer = NewCustomTargetComputer()
                target_container = computer.compute(condition, need_none=True, target_container=target_container,
                                                    industry_container=self.industry_data_container,
                                                    target_express_result=target_express_result)
                if target_container is None:
                    sd.log_error("invalid target_container")
                    continue
                data_list = target_container.data_list
                data_items2 = self._update_custom_target_data_result(target, data_list, custom_record_map)
                if data_items2:
                    data_list_result.extend(data_items2)
        self._update_data_items(data_list_result, company)
        sd.log_info(
            "done _update_company_target0 target={0} size={1} custom_record={2} company={3}".format(
                target.name,
                len(data_list_result), len(custom_record_map), company.company_code))
        return len(data_list_result)

    def _update_custom_target_data_result(self, target, data_list, custom_record_map):
        attr_name = target.field_key
        custom_data = list()
        for data in data_list:
            attr = data.get_attr(attr_name)
            custom_record = self.find_custom_record(data.report_record, custom_record_map)
            item = CustomReportData(report_record_id=custom_record.id, report_model_id=target.id, value=attr)
            custom_data.append(item)
        return custom_data

    def _update_data_items(self, data, company):
        if not data:
            return
        report_record_ids = [x.report_record_id for x in data]
        items = self.target_data_dao.select_custom_target_data0(report_record_ids, data[0].report_model_id,
                                                                CustomReportData)
        sd.log_info("select old custom data size={0} for company={1}".format(len(items), company.company_code))
        item_map = {x.report_record_id: x for x in items}
        new_list = list()
        old_list = list()
        delete_list = list()
        for item in data:
            old = item_map.get(item.report_record_id)
            if not old:
                if item.value is not None:
                    new_list.append(item)
                continue
            if item.value is None:
                delete_list.append(old)
                continue
            if old.value != item.value:
                old.value = item.value
                old.update_time = sd.get_current_second()
                old_list.append(old)
        sd.log_info(
            "_update_data_items all={0} new={1} old={2} data={3} company_code={4}".format(len(items), len(new_list),
                                                                                          len(old_list),
                                                                                          len(data),
                                                                                          company.company_code))
        if new_list:
            CustomReportData.objects.bulk_create(new_list, batch_size=500)
            self.new_count += len(new_list)
        if old_list:
            self.update_count += len(old_list)
            sd.execute_multi_core('update_data_item', self._update_data_item, old_list, 1, True)
        if delete_list:
            self.delete_count += len(delete_list)
            for item in delete_list:
                sd.log_info("delete {0}".format(item))
                item.delete()
        sd.log_info(
            "done _update_data_items all={0} new={1} old={2} delete={3} model_id={4} data={5} company={6}".format(
                len(items),
                len(new_list),
                len(old_list),
                len(delete_list),
                data[0].report_model_id,
                len(data), company.company_code))

    def _update_data_item(self, item):
        sd.log_info("update {}".format(item))
        item.save()

    @sd.try_catch_exception
    def update_record_target(self, custom_record, record, target, old_data):
        computer = NewCustomTargetComputer()
        company = self.company_dao.get_company(record.company_code)
        if not company:
            sd.log_error("update_record_target not found company {}".format(record.company_code))
            return
        cycle_type = record.get_cycle_type()
        combine_type = record.get_combine_type()
        end_year = record.report_year
        start_year = end_year - 3
        condition = TargetCondition(report_time_type=cycle_type, combine_type=combine_type,
                                    compare_target=target, company=company, model_class=target.model_class,
                                    start_year=start_year, end_year=end_year, report_record=record,
                                    report_time_types=get_custom_report_time_types(cycle_type))

        val = computer.compute(condition)
        if val is None:
            sd.log_info("no val for record={0} target={1}".format(record.id, target.id))
            if old_data:
                sd.log_info("delete old val={0} for record={1} target={2}".format(old_data.value, record.id, target.id))
                old_data.delete()
            return

        custom_data = CustomReportData(report_record_id=custom_record.id, report_model_id=target.id, value=val)
        if old_data:
            if old_data.value == custom_data.value:
                return
            old_data.value = custom_data.value
            old_data.save()
            sd.log_info("update custom_data {}".format(old_data))
            return
        custom_data.save()
        sd.log_info("save custom_data {}".format(custom_data))
