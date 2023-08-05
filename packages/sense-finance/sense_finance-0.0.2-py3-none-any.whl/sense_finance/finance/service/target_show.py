from sense_finance.finance.util import *
from sense_finance.finance.dao import *
from sense_finance.finance.model import *
from django.db.models import Q
from sense_finance.finance.target import *


class TargetShowService(object):

    @classmethod
    def company_targets_show(cls, company_code, uid, industry_id=None, is_new=True):
        if industry_id:
            company_model = CompanyModelClass.objects.filter(industry_id=industry_id).first()
            model_class = company_model.model_class if company_model else COMMON_MODEL_CLASS
        else:
            model_class = ComapnyModelClassManager().get_model_class(company_code, use_company=True)
        if not model_class:
            sd.log_info("not model_class found for {0}".format(company_code))
            return list()
        return cls.finance_targets_show(model_class, uid, industry_id=industry_id, is_new=is_new)

    @classmethod
    def finance_targets_show(cls, model_class, uid, industry_id=None, is_new=True):
        targets = list()
        targets_dict = dict()
        if industry_id:
            company_model = CompanyModelClass.objects.filter(industry_id=industry_id).first()
            model_class = company_model.model_class if company_model else COMMON_MODEL_CLASS
        objects = ReportModel.objects.filter(model_class=model_class, row_name_normal__isnull=False).all()
        report_models = cls._check_finance_targets(list(objects.values()))
        if len(report_models) == 0:
            return targets
        for report_model in report_models:
            if report_model['report_name_normal'] not in targets_dict:
                targets_dict[report_model['report_name_normal']] = [
                    [report_model['model_name'], report_model['row_name_normal'], report_model['row_no']]]
            else:
                targets_dict[report_model['report_name_normal']].append(
                    [report_model['model_name'], report_model['row_name_normal'], report_model['row_no']])
        for key, value in targets_dict.items():
            temp_dict = dict()
            temp_dict['name'] = key
            items = cls._agg_report_model(value)
            temp_dict['items'] = items
            temp_dict['sort_no'] = cls._get_table_sort_no(key)
            targets.append(temp_dict)
        targets = cls._add_custom_target(uid, model_class, targets, is_new)
        return targets

    @classmethod
    def _check_finance_targets(cls, targets):
        _res = list()
        if not targets or len(targets) == 0:
            return _res
        for target in targets:
            if not target['report_name_normal'] or len(target['report_name_normal']) == 0:
                continue
            if not target['row_name_normal'] or len(target['row_name_normal']) == 0:
                continue
            _res.append(target)
        return _res

    @classmethod
    def _get_table_sort_no(cls, key):
        if key == '利润表':
            return 1
        elif key == '现金流量表':
            return 2
        elif key == '资产负债表':
            return 3
        elif key == '财务指标表':
            return 4
        elif key == '定制指标表':
            return 100
        else:
            return 5

    @classmethod
    def _agg_report_model(cls, infos):
        _res = list()
        for info in infos:
            _res.append({
                'name': info[1],
                'value': info[1],
                'row_no': info[2],
                'state': 0,
                'pin_yin': chinese_to_pinyin_str(info[1])
            })
        _res = sorted(_res, key=lambda x: x['row_no'])
        return [{'name': '', 'items': _res}]

    @classmethod
    def _agg_custom_target(cls, targets):
        _res = list()
        index = 0
        for target in targets:
            _res.append({
                'name': target.target_name,
                'value': target.target_name,
                'row_no': index,
                'state': 1 if target.is_computing() else 0,
                'pin_yin': chinese_to_pinyin_str(target.target_name)
            })
            index += 1
        _res = sorted(_res, key=lambda x: x['row_no'])
        return [{'name': '', 'items': _res}]

    @classmethod
    def _add_custom_target(cls, uid, model_class, targets, is_new=True):
        custom_targets = list(CustomTarget.objects.filter(Q(create_user=uid, secret_level=0) | Q(secret_level=1)).
                              filter(model_class=model_class).order_by('-create_time').all())
        custom, keep = cls._seprate_keep_targets(custom_targets)
        cls._handle_keep_targets(targets, keep)
        if custom:
            cls._check_target_computing(custom)
        if is_new:
            cls._seprate_custom_targets_nested(uid, custom, targets)
        else:
            cls._seprate_custom_targets_direct(uid, custom, targets)
        targets = sorted(targets, key=lambda x: x['sort_no'], reverse=False)
        return targets

    @classmethod
    def _check_target_computing(cls, targets):
        tasks = TaskQueue.objects.filter(task_type=TASK_TYPE_CUSTOM_TARGET, action_type=TASK_ACTION_ADD).all()
        if not tasks:
            return
        target_ids = set([task.task_id for task in tasks])
        for target in targets:
            if target.id in target_ids:
                target.set_is_computing(True)
            else:
                target.set_is_computing(False)

    @classmethod
    def _seprate_custom_targets_direct(cls, uid, custom, targets):
        if not custom:
            return
        custom_my, custom_other = list(), list()
        for item in custom:
            if item.create_user == uid:
                custom_my.append(item)
            else:
                custom_other.append(item)
        if custom_my:
            items = cls._agg_custom_target(custom_my)
            targets.append({'name': '我的定制表', 'sort_no': 100, 'items': items})
        if custom_other:
            items = cls._agg_custom_target(custom_other)
            targets.append({'name': '共享定制表', 'sort_no': 101, 'items': items})

    @classmethod
    def _seprate_custom_targets_nested(cls, uid, custom, targets):
        if not custom:
            return
        custom_my, custom_other = list(), list()
        for item in custom:
            if item.create_user == uid:
                custom_my.append(item)
            else:
                custom_other.append(item)
        targets2 = list()
        if custom_my:
            items = cls._agg_custom_target(custom_my)
            targets2.append({'name': '我的定制', 'sort_no': 100, 'items': items})
        if custom_other:
            items = cls._agg_custom_target(custom_other)
            targets2.append({'name': '他人共享', 'sort_no': 101, 'items': items})
        targets.append({'name': '定制指标表', 'sort_no': 99, 'items': targets2})

    @classmethod
    def _handle_keep_targets(cls, targets, keep):
        if not keep:
            return
        items = cls._agg_custom_target(keep)
        for target in targets:
            if target['name'] == '补充财务指标表':
                target['name'] = '财务指标表'
                target['items'][0]['items'] = items[0]['items'] + target['items'][0]['items']
                return
        targets.append({'name': '财务指标表', 'sort_no': 4, 'items': items})

    @classmethod
    def _seprate_keep_targets(cls, targets):
        custom = list()
        keep = list()
        for target in targets:
            if target.is_keep_target():
                keep.append(target)
            else:
                custom.append(target)
        return custom, keep
