class BaseCondition(object):

    def __init__(self, company=None, company_list=None,
                 targets=None, combine_type=None, compare_target=None, user_id=0, industry_id=None):
        self.company_list = company_list
        self.combine_type = combine_type
        self.targets = targets
        self.company = company
        self.compare_target = compare_target
        self.user_id = user_id
        self.industry_id = industry_id

    def has_company(self):
        return self.company_list or self.company

    def company_map(self):
        map = dict()
        if self.company:
            map[self.company.company_code] = self.company
        if self.company_list:
            for company in self.company_list:
                map[company.company_code] = company
        return map

    def get_company(self, company_code=None):
        if not company_code:
            if self.company:
                return self.company
            if self.company_list:
                return self.company_list[0]
        if self.company:
            if self.company.company_code == company_code:
                return self.company
        if self.company_list:
            for company in self.company_list:
                if company.company_code == company_code:
                    return company
        return None

    @property
    def company_id(self):
        if self.company is None:
            return None
        return self.company.company_code

    def get_select_basic_targets(self):
        if not self.targets:
            result = list()
        else:
            result = [target for target in self.targets if target.is_basic]
        if not self.compare_target or not self.compare_target.is_basic:
            return result
        for target in result:
            if target.name == self.compare_target.name:
                return result
        result.append(self.compare_target)
        return result

    def get_select_custom_targets(self):
        if not self.targets:
            result = list()
        else:
            result = [target for target in self.targets if not target.is_basic]
        if not self.compare_target or self.compare_target.is_basic:
            return result
        for target in result:
            if target.name == self.compare_target.name:
                return result
        result.append(self.compare_target)
        return result

    def get_select_targets(self):
        if not self.targets:
            result = list()
        else:
            result = [target for target in self.targets]
        if not self.compare_target:
            return result
        for target in result:
            if target.name == self.compare_target.name:
                return result
        result.append(self.compare_target)
        return result

    def get_select_field_targets(self):
        if not self.targets:
            return []
        if not self.compare_target:
            return self.targets
        result = list(self.targets)
        for target in result:
            if target.name == self.compare_target.name:
                return result
        result.append(self.compare_target)
        return result
