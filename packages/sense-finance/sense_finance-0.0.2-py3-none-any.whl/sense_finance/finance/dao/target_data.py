from sense_finance.finance.common import *
from sense_finance.finance.helper import *
from .report_data import ReportDataDAO
from sense_finance.finance.model import *


class TargetDataDAO(object):

    def __init__(self):
        self.report_data_dao = ReportDataDAO()

    def select_custom_target_data0(self, record_ids, model_id, model_class):
        result = list()
        unit = 500
        total = len(record_ids)
        for i in range(int(total / unit) + 1):
            if i * unit >= total:
                break
            if total < (i + 1) * unit:
                ids = record_ids[i * unit:total]
            else:
                ids = record_ids[i * unit:(i + 1) * unit]
            items = model_class.objects.filter(report_model_id=model_id, report_record_id__in=ids).all()
            result.extend(items)
        return result

    def select_industry_record_data(self, condition):
        company_codes = condition.company_ids
        codes = get_sensedeal_company_codes(company_codes)
        items = list()
        if codes:
            items = self._select_industry_record_data0(condition, codes, ReportRecord)
        items2 = self._select_industry_record_data0(condition, company_codes, CustomReportRecord)
        items.extend(items2)
        sd.log_info(
            "select_industry_record_data custom={0} total={1} report_year={2} report_scope={3} report_period={4} company_code={5}".format(
                len(items2), len(items), condition.start_year, condition.combine_type, condition.report_time_type,
                len(company_codes)))
        return items

    def _select_industry_record_data0(self, condition, company_codes, record_class):
        records = list(record_class.objects.filter(report_year=condition.start_year,
                                                   report_scope=condition.combine_type,
                                                   report_period=condition.report_time_type,
                                                   company_code__in=company_codes).all())
        return records

    def select_industry_target_data(self, condition, records=None):
        if records is None:
            records = self.select_industry_record_data(condition)
        if not records:
            return None
        items = self.report_data_dao.find_by_record_model(records, condition.targets)
        sd.log_info(
            "select_industry_target_data data start_year={0} end_year={1} report_scope={2} report_period={3} size={4}".format(
                condition.start_year, condition.end_year, condition.combine_type, condition.report_time_type,
                len(items)))
        return self.build_industry_target_data(records, items, condition.company_map())

    def build_industry_target_data(self, records, datas, company_map):
        if not records or not datas:
            return None
        record_map = {x.key: x for x in records}
        result = SingleIndustryTargetDataMap()
        for item in datas:
            record = record_map[item.record_key]
            company = company_map.get(record.company_code)
            if not company:
                sd.log_error("not found company for {}".format(record.company_code))
                continue
            item2 = SingleTargetItem(company=company, value=item.real_value(record))
            result.add(item.report_model_id, item2)
        return result

    def select_target_compare_result(self, condition, target_container):
        container = TargetCompareContainer()
        if not condition.compare_target:
            return container
        weight_target_id = condition.compare_target.id
        for data in target_container.data_list:
            val = data.get_attr(weight_target_id)
            if not val:
                continue
            container.add(data.time_key, data.company_id, val)
        container.recompute()
        return container

    def select_target_result(self, condition):
        record_items, data_items = self.select_condition_report_data(condition)
        return self.build_target_container_directly(record_items, data_items)

    def build_target_container_directly(self, record_items, data_items):
        target_map = defaultdict(CompanyTargetData)
        record_map = {x.key: x for x in record_items}
        record_data_map = self._build_record_data(record_map, data_items)
        for data in record_data_map.values():
            target_map[data.company_id].append(data)
        return TargetDataContainer(target_map, record_items)

    def build_target_container(self, record_items, data_items, cycle_type, combine_type):
        cycle_types = get_custom_report_time_types(cycle_type)
        record_items2 = list()
        record_ids, custom_record_ids = set(), set()
        for record in record_items:
            if record.report_scope != combine_type:
                continue
            if record.report_period not in cycle_types:
                continue
            record_items2.append(record)
            if isinstance(record, CustomReportRecord):
                custom_record_ids.add(record.id)
            else:
                record_ids.add(record.id)
        if not record_ids and not custom_record_ids:
            return None
        data_items2 = list()
        for data in data_items:
            if isinstance(data, CustomReportData):
                if data.report_record_id in custom_record_ids:
                    data_items2.append(data)
            elif data.report_record_id in record_ids:
                data_items2.append(data)
        if not data_items2:
            return None
        sd.log_info(
            "build_target_container record_items={0} data_items={1} cycle_type={2} combine_type={3} record_items2={4} data_items2={5}".format(
                len(record_items), len(data_items), cycle_type, combine_type, len(record_items2), len(data_items2)))
        return self.build_target_container_directly(record_items2, data_items2)

    def __select_company_report_records(self, record_class, condition, model_no_items=None):
        objects = record_class.objects.filter(company_code=condition.company_id)
        if not condition.check_year_range:
            objects = objects.filter(report_year__gte=condition.select_start_year,
                                     report_year__lte=condition.select_end_year)
        else:
            objects = objects.filter(report_year__gte=condition.select_start_year - 1)
        if condition.combine_type is not None:
            objects = objects.filter(report_scope=condition.combine_type)
        if condition.report_time_types:
            objects = objects.filter(report_period__in=condition.report_time_types)
        if model_no_items:
            objects = objects.filter(model_no__in=model_no_items)
        items = list(objects.order_by('-report_year').all())
        return items

    def _check_year_range_items(self, items, condition, need_sort=True):
        if not condition.check_year_range or not items:
            return items
        if need_sort:
            items = sorted(items, key=lambda x: x.report_year, reverse=True)
        end_year = items[0].report_year
        start_year = condition.select_start_year - (condition.select_end_year - end_year)
        if items[len(items) - 1].report_year >= start_year:
            return items
        result = [item for item in items if item.report_year >= start_year]
        sd.log_info("_check_year_range_items from size={0} to {1} with end_year={2} start_year={3}".format(len(result),
                                                                                                           len(items),
                                                                                                           end_year,
                                                                                                           start_year))
        return result

    def _rebuild_check_year_records(self, condition, items):
        if not condition.check_year_range or not items:
            return items
        end_year = items[0].report_year
        if end_year != condition.select_end_year:
            return items
        items = [item for item in items if item.report_year >= condition.select_start_year]
        return items

    def select_targets_datas(self, targets, record_map, query_by_record=False):
        result = list()
        for target in targets:
            items = self.select_target_datas(target, record_map, query_by_record)
            result.extend(items)
        return result

    def select_target_datas(self, target, record_map, query_by_record=False):
        if query_by_record:
            result = self._select_target_datas0_by_records(target, record_map)
            sd.log_info(
                "select_target_datas size={0} by record_map={1} for target={2}".format(len(result), len(record_map),
                                                                                       target.id))
            return result
        result = list()
        self.select_target_datas0(target, record_map, result)
        return result

    def _select_target_datas0_by_records(self, target, record_map):
        if target.is_custom:
            record_ids = [record.id for record in record_map.values() if type(record) == CustomReportRecord]
            if not record_ids:
                return list()
            return self.select_target_data_by_record_ids(CustomReportData, target.id, record_ids)
        result = list()
        record_ids = [record.id for record in record_map.values() if type(record) == ReportRecord]
        if record_ids:
            result.extend(self.select_target_data_by_record_ids(ReportData, target.id, record_ids))
        return result

    def select_target_datas0(self, target, record_map, result):
        if target.is_custom:
            data_classes = [CustomReportData]
        else:
            data_classes = [ReportData]
        for data_class in data_classes:
            self._select_record_data(data_class, target, record_map, result)

    def select_target_records(self, record_classes, combine_type=None, report_time_types=None, model_class=None,
                              report_year=0, model_no=None):
        result = list()
        for record_class in record_classes:
            self.select_combine_type_records(result, record_class, combine_type, report_time_types, model_class,
                                             report_year,model_no)
        return result

    def select_combine_type_records(self, result, record_class, combine_type=None, report_time_types=None,
                                    model_class=None, report_year=0, model_no=None):
        last_id = 0
        limit = 1000 if sd.is_debug() else 10000
        size = 0
        while True:
            items = self._select_single_combine_type_records(record_class, last_id, limit, combine_type,
                                                             report_time_types, model_class, report_year, model_no)
            item_size = len(items)
            if model_class == COMMON_MODEL_CLASS:
                result.extend([item for item in items if item.model_class == COMMON_MODEL_CLASS])
            else:
                result.extend(items)
            size += len(items)
            if item_size < limit:
                break
            last_id = items[len(items) - 1].id
        sd.log_info(
            "select_combine_type_records result size={0} for record_class={1} combine_type={2} report_time_types={3} model_class={4}".format(
                size, record_class, combine_type, report_time_types, model_class))

    def _select_record_data(self, data_class, target, record_map, result):
        last_id = 0
        limit = 1000 if sd.is_debug() else 10000
        while True:
            items = self._select_singel_record_data(data_class, target, last_id, limit)
            for item in items:
                if item.record_key in record_map:
                    result.append(item)
            if len(items) < limit:
                break
            last_id = items[len(items) - 1].id

    def _select_singel_record_data(self, data_class, target, last_id, limit):
        times = 5
        while times >= 0:
            times -= 1
            try:
                return self._select_singel_record_data0(data_class, target, last_id, limit)
            except Exception as ex:
                sd.log_exception(ex)
                sd.sleep(2)
        raise Exception("_select_singel_record_data failed")

    def select_target_data_by_record_ids(self, data_class, target_id, record_ids):
        result = list()
        unit = 1000
        total = len(record_ids)
        for i in range(int(total / unit) + 1):
            if i * unit >= total:
                break
            if total < (i + 1) * unit:
                ids = record_ids[i * unit:total]
            else:
                ids = record_ids[i * unit:(i + 1) * unit]
            items = list(data_class.objects.filter(report_model_id=target_id, report_record_id__in=ids).all())
            result.extend(items)
        sd.log_info(
            "select_target_data_by_record_ids data_class={0} target_id={1} record_ids={2} size={3}".format(
                data_class, target_id, len(record_ids), len(result)))
        return result

    def _select_singel_record_data0(self, data_class, target, last_id, limit):
        items = data_class.objects.filter(report_model_id=target.id).filter(id__gt=last_id).order_by('id').all()[
                0:limit]
        sd.log_info(
            "_select_record_data size={0} for last_id={1} limit={2} target={3}".format(len(items), last_id, limit,
                                                                                       target.id))
        return items

    def _select_single_combine_type_records(self, record_class, last_id, limit, combine_type=None,
                                            report_time_types=None, model_class=None, report_year=0, model_no=None):
        objects = record_class.objects
        if model_class and model_class != COMMON_MODEL_CLASS:
            objects = objects.filter(model_class=model_class)
        if combine_type:
            objects = objects.filter(report_scope=combine_type)
        if report_year > 0:
            objects = objects.filter(report_year=report_year)
        if model_no:
            objects = objects.filter(model_no=model_no)
        if report_time_types:
            if len(report_time_types) == 1:
                objects = objects.filter(report_period=report_time_types[0])
            else:
                objects = objects.filter(report_period__in=report_time_types)
        objects = objects.filter(id__gt=last_id).order_by('id').all()[0:limit]
        sd.log_info(
            "_select_single_combine_type_records size={0} for record_class={1} last_id={2} limit={3} combine_type={4} report_time_types={5} report_year={6}".format(
                len(objects), record_class, last_id, limit, combine_type, report_time_types, report_year))
        return objects

    def _need_custom_report_record(self, targets):
        if not targets:
            return True
        for target in targets:
            if target.is_custom:
                return True
        return False

    def _get_basic_model_no_items(self, targets):
        if not targets:
            return None
        items = set()
        for target in targets:
            if target.is_custom or not target.model_no:
                continue
            items.add(target.model_no)
        if not items:
            return None
        return list(items)

    def _select_report_records(self, condition, targets=None):
        items = list()
        model_no_items = self._get_basic_model_no_items(targets)
        if not condition.company_ids:
            items = self.__select_company_report_records(ReportRecord, condition, model_no_items)
            if self._need_custom_report_record(targets):
                items.extend(self.__select_company_report_records(CustomReportRecord, condition))
            items = self._check_year_range_items(items, condition, False)
        else:
            codes = get_sensedeal_company_codes(condition.company_ids)
            if codes:
                items = self._select_report_records0(codes, condition, ReportRecord)
            if self._need_custom_report_record(targets):
                items.extend(self._select_report_records0(condition.company_ids, condition, CustomReportRecord))
            items = self._check_year_range_items(items, condition, True)
        sd.log_info(
            "_select_report_records size={0} for company_id={6},company_codes={1} for select_start_year={2} select_end_year={3} combine_type={4} report_time_types={5} check_year_range={6}".format(
                len(items), len(condition.company_ids), condition.select_start_year, condition.select_end_year,
                condition.combine_type, condition.report_time_types, condition.check_year_range))
        return items

    def _select_report_records0(self, company_ids, condition, record_class):
        result = list()
        unit = 1000
        total = len(company_ids)
        select_start_year = condition.select_start_year
        if condition.check_year_range:
            select_start_year -= 1
        for i in range(int(total / unit) + 1):
            if i * unit >= total:
                break
            if total < (i + 1) * unit:
                ids = company_ids[i * unit:total]
            else:
                ids = company_ids[i * unit:(i + 1) * unit]
            items = list(record_class.objects.filter(report_year__gte=select_start_year,
                                                     report_year__lte=condition.select_end_year,
                                                     report_scope=condition.combine_type,
                                                     report_period__in=condition.report_time_types,
                                                     company_code__in=ids).all())
            result.extend(items)
            sd.log_info(
                "_select_report_records0 record_class={0} i={1} company_ids={2} size={3} select_start_year={4}".format(
                    record_class, i, len(company_ids), len(items), select_start_year))
        return result

    def select_condition_report_data(self, condition):
        targets = condition.get_select_targets()
        record_items = self._select_report_records(condition, targets)
        if not record_items:
            return list(), list()
        result = self.report_data_dao.find_by_record_model(record_items, targets)
        sd.log_info(
            "select_condition_report_data size={0} record_items={1} target size={2}".format(len(result),
                                                                                            len(record_items),
                                                                                            len(targets),
                                                                                            ))
        return record_items, result

    def _build_record_data(self, record_map, data_items):
        result = dict()
        for item in data_items:
            record = record_map.get(item.record_key)
            if not record:
                continue
            key = "{0}_{1}_{2}".format(record.company_code, record.report_year, record.report_period)
            data = result.get(key)
            if not data:
                data = TargetData(report_year=record.report_year, report_month=record.report_real_month,
                                  report_time_type=record.report_period, company_id=record.company_code,
                                  combine_type=record.report_scope, report_record=record)
                result[key] = data
            data.add_attr(item.report_model_id, item.real_value(record))
        sd.log_info("_build_record_data size={0} record_size={1} data_items={2}".format(len(result),
                                                                                        len(record_map),
                                                                                        len(data_items)))
        return result
