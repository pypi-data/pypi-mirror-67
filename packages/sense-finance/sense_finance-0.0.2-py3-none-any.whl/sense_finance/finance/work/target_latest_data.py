import sense_core as sd
from sense_finance.finance.util import *
from sense_finance.finance.model import *
from sense_finance.finance.target import TargetLatestDataUpdater2
from sense_finance.finance.dao import *



class CompanyTargetLatestDataWorker(object):

    @sd.try_catch_exception
    def update_all_company_industry(self):
        sd.log_info("start update_all_company_industry")
        start_time = sd.get_current_second()
        items = CompanyDAO().get_finance_all()
        sd.log_info("get company size={}".format(len(items)))
        sd.execute_multi_core("xx", self.update_company_industry, items, 4, True)
        sd.log_info("end update_all_company_industry cost={0}".format(sd.get_current_second() - start_time))

    def update_company_code_industry(self, company_code):
        company = CompanyDAO().get_company(company_code)
        if not company:
            return
        self.update_company_industry(company)

    def update_company_industry(self, company):
        data = CompanyTargetLatestData.objects.filter(company_code=company.company_code).order_by(
            '-report_year').first()
        if not data:
            return
        first_industry_code = strip_industry_id(company.first_industry_code)
        second_industry_code = strip_industry_id(company.second_industry_code)
        three_industry_code = strip_industry_id(company.three_industry_code)
        four_industry_code = strip_industry_id(company.four_industry_code)

        if data.first_industry_code != first_industry_code:
            CompanyTargetLatestData.objects.filter(company_code=company.company_code).update(
                first_industry_code=first_industry_code)
            sd.log_info(
                "update_company_industry first_industry_code={0} company={1}".format(first_industry_code,
                                                                                     company.company_code))
        if data.second_industry_code != second_industry_code:
            CompanyTargetLatestData.objects.filter(company_code=company.company_code).update(
                second_industry_code=second_industry_code)
            sd.log_info(
                "update_company_industry second_industry_code={0} company={1}".format(second_industry_code,
                                                                                      company.company_code))
        if data.three_industry_code != three_industry_code:
            sd.log_info("not same three_industry_code 0={0} 1={1}".format(data.three_industry_code,
                                                                          three_industry_code))
            CompanyTargetLatestData.objects.filter(company_code=company.company_code).update(
                three_industry_code=three_industry_code)
            sd.log_info(
                "update_company_industry three_industry_code={0} company={1}".format(three_industry_code,
                                                                                     company.company_code))
        if data.four_industry_code != four_industry_code:
            sd.log_info("not same four_industry_code 0={0} 1={1}".format(data.four_industry_code,
                                                                         four_industry_code))
            CompanyTargetLatestData.objects.filter(company_code=company.company_code).update(
                four_industry_code=four_industry_code)
            sd.log_info(
                "update_company_industry four_industry_code={0} company={1}".format(four_industry_code,
                                                                                    company.company_code))
        sd.log_info("done update_company_industry for {}".format(company.company_code))

    def build_all(self):
        start_time = sd.get_current_second()
        sd.log_info("start CompanyTargetLatestDataWorker")
        thread_num = 4
        items = CompanyInfo.find_all()
        sd.log_info("got CompanyInfo size={0}".format(len(items)))
        sd.execute_multi_core("target_data", self.build_company, items, thread_num, True)
        sd.log_info("CompanyTargetLatestDataWorker done cost={0}".format((sd.get_current_second() - start_time) / 60))

    @sd.try_catch_exception
    def build_company(self, company):
        handler = TargetLatestDataUpdater2()
        handler.update_by_company_code(company)
