from sense_django.request_utils import *


@catch_view_exception
def finance_select_params(request):
    result = RequestResult()
    uid = get_user_id(request)
    company_code = parse_param(request, 'company_code')
    sd.log_info("finance_select_params uid={0} company_code={1}".format(uid, company_code))
    data = FinanceService.get_finance_select_params(uid, company_code)
    return build_response(result.set_data(data))


@catch_view_exception
def industry_select_params(request):
    result = RequestResult()
    uid = get_user_id(request)
    company_code = parse_param(request, 'company_code')
    industry_id = parse_param(request, 'industry_id')
    data = FinanceService.get_industry_select_params(uid, company_code, industry_id)
    return build_response(result.set_data(data))


@catch_view_exception
def finance_statistics(request):
    result = RequestResult()
    uid = get_user_id(request)
    params = parse_finance_targets_params(request)
    try:
        condition, statistics_items = CompanyTargetComputeService.compute(params)
        params['targets'] = [x.param_name() for x in condition.targets]
        if 'use_default' not in params and 'target_items' in statistics_items and len(
                statistics_items['target_items']) > 0:
            FinanceService.save_user_view_config(uid, VIEW_TYPE_COMPANY_REPORT, params)
        result.add_data_item('statistics_items', statistics_items)
        result.add_data_item('config_params', params)
    except Exception as ex:
        sd.log_exception(ex)
        return build_response(result.set_error(str(ex)))
    return build_response(result)


@catch_view_exception
def finance_industry_analysis(request):
    result = RequestResult()
    try:
        uid = get_user_id(request)
        params = parse_industry_analysis_params(request)
        condition, industry_analysis = IndustryCompanyTargetService.compute(params)
        if not industry_analysis:
            params['targets'] = []
            params['target_show'] = []
            result.add_data_item('config_params', params)
            return build_response(result)
        params['targets'] = [x.param_name() for x in condition.targets]
        if 'use_default' not in params and industry_analysis and 'company_targets' in industry_analysis and len(
                industry_analysis['company_targets']) > 0:
            FinanceService.save_user_view_config(uid, VIEW_TYPE_INDUSTRY_REPORT, params)
        result.add_data_item('industry_analysis', industry_analysis)
        params['target_show'] = [{'id': x.id, 'name': x.name} for x in condition.targets]
        result.add_data_item('config_params', params)
    except Exception as ex:
        sd.log_exception(ex)
        result.set_error_code(RequestResult.SYSTEM_ERROR)
    return build_response(result)
