import sense_core as sd
from sense_finance.finance.common import *
from sense_finance.finance.model import IndustryTargetData


class TargetIndustryValueComputer(object):

    def __init__(self, industry_container):
        self.industry_container = industry_container

    def compute_industry_body_value(self, item, condition, target_body, target, report_year, report_period):
        company = condition.get_company(item.company_id)
        if not company:
            sd.log_error("compute_industry_body_value not found company code {}".format(item.company_id))
            return None
        target_type = get_industry_target_type(target_body)
        if is_first_industry_target_type(target_body):
            industry_id = company.first_industry_code
        else:
            industry_id = company.second_industry_code
        if not target_type or not industry_id:
            return None
        if self.industry_container:
            data = IndustryTargetData()
            data.report_scope = condition.combine_type
            data.report_period = report_period
            data.report_year = report_year
            data.report_model_id = target.id
            data.target_type = target_type
            data.industry_id = industry_id
            return self.industry_container.get_value(data)
        item = IndustryTargetData.objects.filter(
            industry_id=industry_id,
            report_scope=condition.combine_type,
            report_year=report_year,
            report_period=report_period,
            report_model_id=target.id).first()
        if not item:
            sd.log_info(
                "compute_industry_body_value none for industry_id={0} report_scope={1},report_period={2} report_year={3} report_model_id={4} company={5}".format(
                    industry_id, condition.combine_type, report_period, report_year, target.id, company.company_code))
            return None
        if sd.is_debug():
            sd.log_info(
                "compute_industry_body_value get {0} company={1} ".format(item, company.company_code))
        return item.value
