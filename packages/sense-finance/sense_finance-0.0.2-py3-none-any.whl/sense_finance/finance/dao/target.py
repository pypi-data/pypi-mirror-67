from sense_finance.finance.common import *
from sense_finance.finance.helper import *
from sense_finance.finance.model import *


class TargetDAO(object):

    def find_public_custom_targets(self, model_class=None, min_id=0):
        if model_class:
            objects = CustomTarget.objects.filter(model_class=model_class)
        else:
            objects = CustomTarget.objects
        if min_id > 0:
            objects = objects.filter(id__gt=min_id)
        return list(objects.order_by('id').all())

    def find_targets_by_ids(self, ids):
        custom_ids = [id for id in ids if is_custom_target_range(id)]
        if custom_ids:
            targets = list(CustomTarget.objects.filter(id__in=ids).all())
            if len(custom_ids) == len(ids):
                return targets
        else:
            targets = list()
        normal_ids = [id for id in ids if not is_custom_target_range(id)]
        if normal_ids:
            targets2 = list(ReportModel.objects.filter(id__in=ids).all())
            if targets2:
                targets.extend(targets2)
        return targets

    def find_target(self, id):
        if is_custom_target_range(id):
            return CustomTarget.find_by_id(id)
        return ReportModel.find_by_id(id)

    def _find_custom_targets_by_name(self, name, model_class=None):
        objects = CustomTarget.objects.filter(target_name=refine_target_name(name))
        if model_class:
            objects = objects.filter(model_class=model_class)
        return filter_targets(objects.all())

    def _find_basic_targets_by_name(self, name, model_class=None):
        objects = ReportModel.objects.filter(row_name_normal=refine_target_name(name))
        if model_class:
            objects = objects.filter(model_class=model_class)
        return filter_targets(objects.all())

    def _find_basic_targets_by_names(self, names, model_class=None):
        objects = ReportModel.objects.filter(row_name_normal__in=names)
        if model_class:
            objects = objects.filter(model_class=model_class)
        return filter_targets(objects.all())

    def _find_custom_targets_by_names(self, names, model_class=None):
        objects = CustomTarget.objects.filter(target_name__in=names)
        if model_class:
            objects = objects.filter(model_class=model_class)
        return filter_targets(objects.all())

    def find_targets_by_name(self, name, model_class=None):
        targets = self._find_basic_targets_by_name(name, model_class)
        if not targets:
            return self._find_custom_targets_by_name(name, model_class)
        return targets

    def find_targets_by_names(self, names, model_class=None):
        targets = self._find_basic_targets_by_names(names, model_class)
        if len(targets) == len(names):
            return self._sort_targets(targets, names)
        target_map = {target.name: target for target in targets}
        names2 = [name for name in names if name not in target_map]
        if not names2:
            return self._sort_targets(targets, names)
        targets2 = self._find_custom_targets_by_names(names2, model_class)
        return self._sort_targets(targets + targets2, names)

    def _sort_targets(self, targets, names):
        target_map = {target.name: target for target in targets}
        result = list()
        for name in names:
            target = target_map.get(name)
            if target:
                result.append(target)
        return result
