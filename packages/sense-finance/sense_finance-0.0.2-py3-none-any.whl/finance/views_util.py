from sense_django.request_utils import *


def parse_monit_log_params(request):
    uid = get_user_id(request)
    pn = parse_int_param(request, 'pn')
    if pn < 0:
        pn = 0
    size = parse_int_param(request, 'size')
    if size < 5 or size > 100:
        size = 30
    monit_id = parse_int_param(request, 'monit_id')
    filter_type = parse_int_param(request, 'filter_type')
    monit_type = parse_int_param(request, 'monit_type')
    message_id = parse_param(request, 'message_id')
    company_code = parse_param(request, 'company_code')
    spread_uid = parse_param(request, 'spread_uid')
    return {
        'uid': uid,
        'pn': pn,
        'size': size,
        'monit_id': monit_id,
        'monit_type': monit_type,
        'message_id': message_id,
        'company_code': company_code,
        'filter_type': filter_type,
        'spread_uid': spread_uid,
    }


def _parse_targets_params0(request):
    params = dict()
    params['targets'] = parse_list_param(request, 'targets')
    params['uid'] = get_user_id(request)
    params['industry_range'] = parse_param(request, 'industry_range')
    params['ratio_type'] = parse_int_param(request, 'ratio_type', 0)
    params['report_time_type'] = parse_int_param(request, 'report_time_type', REPORT_CYCLE_PERIOD)
    params['time_range_type'] = parse_int_param(request, 'time_range_type', REPORT_TIME_RANGE_THREE)
    params['company_code'] = parse_param(request, 'company_code')
    is_test = parse_int_param(request, 'is_test')
    if is_test == 1:
        params['is_test'] = 1
    return params


def parse_finance_targets_params(request):
    params = _parse_targets_params0(request)
    params['combine_type'] = parse_int_param(request, 'combine_type', REPORT_BORE_COMBINE)
    params['compare_type'] = parse_int_param(request, 'compare_type', COMPARE_MEAN_SIMPLE)
    return params


def parse_list_param(request, name):
    range = parse_param(request, name)
    if len(range) > 1:
        range = range.split(',')
    else:
        range = list()
    return range


def parse_industry_analysis_params(request):
    params = _parse_targets_params0(request)
    params['limit_type'] = parse_int_param(request, 'limit_type', LIMIT_TYPE_TOP5)
    params['compare_type'] = parse_int_param(request, 'compare_type', COMPANY_COMPARE_TYPE_TOP)
    params['compare_target'] = parse_param(request, 'compare_target')
    params['industry_id'] = parse_param(request, 'industry_id')
    params['combine_type'] = parse_int_param(request, 'combine_type', REPORT_BORE_COMBINE)
    return params


def parse_custom_target_add_params(request):
    params = dict()
    params['uid'] = get_user_id(request)
    params['target_id'] = parse_int_param(request, 'target_id')
    params['dim_type'] = parse_int_param(request, 'dim_type', ROW_DIM_NO)
    params['name'] = parse_param(request, 'name')
    params['explain'] = parse_param(request, 'explain')
    params['secret_level'] = TARGET_STATUS_PUBLIC
    params['target'] = parse_param(request, 'target')
    params['target_status'] = TARGET_STATUS_PUBLIC
    params['model_class'] = parse_param(request, 'model_class')
    return params


def parse_custom_monitor_add_params(request):
    params = dict()
    params['uid'] = get_user_id(request)
    params['name'] = parse_param(request, 'name')
    params['monitor_id'] = parse_int_param(request, 'monitor_id')
    params['monitor_target'] = parse_param(request, 'monitor_target')
    params['monitor_msg'] = parse_param(request, 'monitor_msg')
    params['monitor_status'] = parse_int_param(request, 'monitor_state', -1)
    if params['monitor_status'] < 0:
        params['monitor_status'] = parse_int_param(request, 'monitor_status')
    params['monit_range'] = parse_list_param(request, 'monit_range')
    params['model_class'] = parse_param(request, 'model_class')
    params['is_spread'] = parse_int_param(request, 'is_spread')
    params['spread_range'] = parse_list_param(request, 'spread_range')
    return params


def _build_user_stock_finance_config(params):
    user_config = dict()
    user_config['report_time_type'] = params['report_time_type']
    user_config['time_range_type'] = params['time_range_type']
    user_config['combine_type'] = params['combine_type']
    user_config['compare_type'] = params['compare_type']
    user_config['targets'] = params['targets']
    report_models = ReportModel.objects.filter(id__in=params['targets']).all()
    items = sd.build_model_list(report_models, type='config')
    user_config['targets_show'] = items
    return user_config


def _build_user_industry_analysis_config(params):
    user_config = dict()
    user_config['report_time_type'] = params['report_time_type']
    user_config['time_range_type'] = params['time_range_type']
    user_config['company_compare_type'] = params['company_compare_type']
    user_config['limit_type'] = params['limit_type']
    user_config['targets'] = params['targets']
    report_models = ReportModel.objects.filter(id__in=params['targets']).all()
    items = sd.build_model_list(report_models, type='config')
    user_config['targets_show'] = items
    return user_config
