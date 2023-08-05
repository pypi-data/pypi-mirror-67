import pypinyin
import sense_core as sd
import datetime
import time
from sense_core import Encryption
import re
import uuid
import logging
from math import *


def init_config(module_name=''):
    monit_queue = 'rabbit_monit' if not sd.is_debug() else ''
    sd.log_init_config(project_name(), sd.config('log_path'), monit_queue=monit_queue, use_module_name=module_name)
    sd.set_report_error_log(True)
    logging.getLogger("pika").propagate = False


def project_name():
    return sd.config('project_name')


def is_sensedeal_env():
    return True


def get_valid_text(text, default='-'):
    return text if text else default



def format_money_value(val, format=2, devide=10000, default_value='-'):
    if not val:
        return default_value
    if devide:
        val = val / devide
    if int(val) == val:
        val = int(val)
    elif format:
        val = format_float(val, format)
    return format_number_sep(val)


def format_number_sep(str):
    return "{:,}".format(str)


def strip_industry_id(id):
    return id.strip() if id else ""


def convert_second_time(timestamp):
    if len(str(timestamp)) <= 10:
        return timestamp
    return int(timestamp[0:10])


def is_same_dict(dict1, dict2):
    if dict1 == dict2:
        return True
    if dict1 is None or dict2 is None:
        return False
    if len(dict1) != len(dict2):
        return False
    if type(dict1) == list:
        for i in range(len(dict1)):
            if dict1[i] != dict2[i]:
                return False
        return True
    for k, v in dict1.items():
        if k == 'updated_time':
            continue
        v2 = dict2.get(k)
        if v == v2:
            continue
        if v is None or v2 is None:
            return False
        if type(v) == datetime.datetime or type(v2) == datetime.datetime:
            if not is_same_date(v, v2):
                return False
            continue
        if type(v) != type(v2):
            return False
        if type(v) == list or type(v) == dict:
            if not is_same_dict(v, v2):
                return False
        return False
    return True


def is_same_date(date1, date2):
    if type(date1) != datetime.datetime:
        date1 = sd.parse_date(date1)
    if type(date2) != datetime.datetime:
        date2 = sd.parse_date(date2)
    return date1.year == date2.year and date1.month == date2.month and date1.day == date2.day


def is_float(str):
    try:
        float(str)
        return True
    except:
        return False


def is_chinese_char(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


def is_chinese_text(text):
    for c in text:
        if not is_chinese_char(c):
            return False
    return True


def parse_custom_target_format(str):
    index = str.find(':')
    if index == 1 and len(str) > 2:
        return str[2:len(str)]
    return str


def parse_config(label, key, need_decrpt=True):
    val = sd.config(label, key, '')
    if sd.is_debug() or not need_decrpt or not val:
        return val
    return Encryption.decrypt_key(val)


def parse_label_config(label, encrypt_keys):
    host = parse_config(label, 'host', 'host' in encrypt_keys)
    port = parse_config(label, 'port', 'port' in encrypt_keys)
    user = parse_config(label, 'user', 'user' in encrypt_keys)
    password = parse_config(label, 'pass', 'pass' in encrypt_keys)
    if not password:
        password = parse_config(label, 'password', 'password' in encrypt_keys)
    return {
        'host': host,
        'port': port,
        'user': user,
        'pass': password,
    }


def get_current_hour():
    now = datetime.datetime.now()
    return now.hour


def format_zh_time(time):
    d1 = datetime.datetime.now()
    d2 = datetime.datetime.fromtimestamp(time)
    diff = int(round(d1.timestamp() - time))
    if diff < 60:
        return '刚刚'
    min = diff / 60
    if min < 60:
        return str(int(min)) + '分钟前'
    hour = diff / 3600
    if hour < 24 and d1.day == d2.day:
        return str(int(hour)) + '小时前'
    return d2.strftime('%Y-%m-%d')


def is_in_option_values(val, items, default_value=None):
    val2 = parse_int(val, default_value)
    if val2 is not None:
        val = val2
    for item in items:
        if val == item['value']:
            return True
    return False


def get_in_option_value(val, items, default_value=None):
    val2 = parse_int(val, default_value)
    if val2 is not None:
        val = val2
    for item in items:
        if val == item['value']:
            return item['name']
    return None


def parse_float(val, default=0):
    try:
        return float(val)
    except:
        return default


def parse_int(val, default=0):
    try:
        return int(val)
    except:
        return default


def chinese_to_pinyin(word, first=True):
    _res = []
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        if first:
            _res.extend(i[0][0])
        else:
            _res.extend(i)
    return _res


def chinese_to_pinyin_str(word, first=True):
    if not word:
        return ''
    return ''.join(chinese_to_pinyin(word, first))


def format_shares(all_pledge_num, unit='股'):
    if not all_pledge_num:
        return 0
    if all_pledge_num >= 100000000:
        all_pledge_num = str(float('%.2f' % (all_pledge_num / 100000000))) + '亿' + unit
    elif all_pledge_num >= 10000:
        all_pledge_num = str(float('%.2f' % (all_pledge_num / 10000))) + '万' + unit
    else:
        all_pledge_num = str(int(all_pledge_num)) + unit
    return all_pledge_num


def get_accum_value(list1, key):
    _res = 0
    try:
        for item in list1:
            value = item.get(key, 0)
            if value:
                _res += value
        _res = float('%.2f' % _res)
    except Exception as ex:
        sd.log_exception(ex)
    return _res


def get_str_ratio(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        return '%.2f' % (num1 * 100 / num2)
    except:
        return '0'


def get_pledge_mean(value, num):
    try:
        value = float(value)
        num = float(num)
        return '%.2f' % (value / num)
    except:
        return '0'


def str_to_float(str1):
    try:
        return float(str1)
    except:
        return float(0)


def build_time_output(time1, type=False):
    if not time1 or time1 == '':
        return ''
    now = datetime.datetime.now()
    today_start = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                           microseconds=now.microsecond)
    today_end = today_start + datetime.timedelta(hours=24)
    today_start = round(today_start.timestamp())
    today_end = round(today_end.timestamp())
    if time1 > today_end:
        if type:
            return sd.timestamp_to_str(datetime.datetime.now().timestamp(), format="%H:%M")
        return sd.timestamp_to_str(datetime.datetime.now().timestamp(), format="%H:%M:%S")
    if time1 > today_start:
        if type:
            return sd.timestamp_to_str(time1, format="%H:%M")
        return sd.timestamp_to_str(time1, format="%H:%M:%S")
    else:
        return sd.timestamp_to_str(time1, format="%Y-%m-%d")


def build_year_agg(time1):
    if not time1 or time1 == '':
        return None, None
    now = datetime.datetime.now()
    today_start = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                           microseconds=now.microsecond)
    today_start = round(today_start.timestamp())
    if time1 > today_start:
        time_str = sd.timestamp_to_str(time1, format="%H:%M")
        year = str(get_current_year())
    else:
        year = sd.timestamp_to_str(time1, format="%Y")
        time_str = sd.timestamp_to_str(time1, format="%m-%d")
    return year, time_str


def get_today_start_time():
    now = datetime.datetime.now()
    today_start = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                           microseconds=now.microsecond)

    return today_start


def get_report_year(time1):
    try:
        time_str = str(time1)
        return time_str[0:4]
    except:
        return '-'


def convert_target_value(value):
    if value:
        return value
    else:
        return 0


def get_ago_year_list(n):
    year_list = [time.strftime('%Y', time.localtime(time.time() - 3600 * 24 * 365 * num)) for num in
                 range(n - 1, -1, -1)]
    return year_list


def get_user_id(request):
    try:
        return str(request.user.user_id)
    except Exception as ex:
        print(ex)
        return ''


def build_pd_records(each):
    temp = each.to_dict('records')
    return temp


def build_pd_list(each):
    temp = each.to_list()
    return temp


def get_current_year():
    return datetime.datetime.now().year


def compute_accum_num(result, key):
    _res = 0
    try:
        for each in result:
            if each[key]:
                _res += each[key]
        return round(_res, 2)
    except:
        return _res


def format_float(val, keep=6):
    return round(val, keep)


def sort_pd_id(items):
    result = sorted(items, key=lambda x: x['id'])
    return result


def convert_time_output(time1):
    try:
        _res = time1.strftime('%Y-%m-%d')
        return _res
    except:
        return time1


def money_format(money):
    try:
        money = '%.2f' % money
        money_parts = money.split('.')
        integer_part = money_parts[0]
        integer_part_length = len(integer_part)
        n = (integer_part_length - 1) // 3 + 1
        parts = [integer_part[(i - n) * 3:integer_part_length - (n - i) * 3 + 3] for i in range(n)]
        money_parts[0] = ','.join(parts)
        res = '.'.join(money_parts)
        if res[0] and res[0] == '-' and res[1] == ',':
            res = res[0:1] + res[2:]
        return res
    except:
        return '-'


def get_division(value1, value2):
    try:
        value1 = float(value1)
        value2 = float(value2)
        res = '%.2f' % (value1 / value2)
        return float(res)
    except:
        return 0


def filter_html_tag(html, tag_name=''):
    if tag_name == '':
        return re.sub(r'</?\w+[^>]*>', '', html)
    return re.sub(r'</?' + tag_name + '>', '', html)


def get_day_list(time_range):
    date_list = list()
    begin_date = (datetime.datetime.now() - datetime.timedelta(days=time_range)).strftime("%Y-%m-%d")
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(time.strftime('%Y-%m-%d', time.localtime(time.time())), "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list


def get_day_start(date):
    # return date.replace(hour=0, minute=0, second=0)
    try:
        return datetime.datetime.combine(date, datetime.time.min)
    except Exception as ex:
        sd.log_error("get_day_start bad time:{}".format(date))
        return 0


def get_day_end(date):
    # return date.replace(hour=23, minute=59, second=59)
    try:
        return datetime.datetime.combine(date, datetime.time.max)
    except Exception as ex:
        sd.log_error("get_day_end bad time:{}".format(date))
        return 0


def get_day_start_time(timestamp):
    return int(round(get_day_start(datetime.datetime.fromtimestamp(timestamp)).timestamp()))


def get_day_end_time(timestamp):
    return int(round(get_day_end(datetime.datetime.fromtimestamp(timestamp)).timestamp()))


def get_day_int(timestamp, format='%Y%m%d'):
    if not timestamp:
        date = datetime.datetime.now()
    else:
        date = datetime.datetime.fromtimestamp(timestamp)
    return int(date.strftime(format))


def get_news_id(url):
    news_id = uuid.uuid5(uuid.NAMESPACE_OID, url).__str__()
    return news_id


def convert_num_unit(num):
    try:
        num = float(num)
        if not num:
            return '0'
        elif num >= 100000000:
            return '{}亿'.format(round(num / 100000000, 2))
        elif num >= 10000:
            return '{}万'.format(round(num / 10000, 2))
        return '{}'.format(num)
    except:
        return '{}'.format(num)


def get_num_unit(num):
    try:
        num = float(num)
        if not num:
            return ''
        elif num >= 100000000:
            return '亿'
        elif num >= 10000:
            return '万'
        return ''
    except:
        return ''


def build_num_output(value):
    if not value:
        return value, ''
    elif value[-1] == '万':
        return value[:-1], '万'
    elif value[-1] == '亿':
        return value[:-1], '亿'
    return value, ''


# input Lat_A 纬度A
# input Lng_A 经度A
# input Lat_B 纬度B
# input Lng_B 经度B
# output distance 距离(km)
def calc_loc_distance(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r


@sd.try_catch_exception
def log_task_schedule(task_name, period=3600 * 30, exclude_time=None):
    if sd.is_debug() or not is_sensedeal_env():
        return
    if not exclude_time:
        exclude_time = "0-9"
    sd.log_task_schedule(task_name, period, module='wind_eye', exclude_time=exclude_time)
