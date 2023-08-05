from sense_finance.finance.custom.core import *


def parse_target_body(name):
    index = name.rfind('的')
    if index <= 0:
        return name, TARGET_BODY_COMPANY
    post = name[index + 1:]
    body_type = get_target_body_type(post)
    if body_type is None:
        return name, TARGET_BODY_COMPANY
    return name[0:index], body_type


def parse_target_lost_type(name):
    index = name.rfind('^')
    if index <= 0:
        return TARGET_LOST_DEFAULT, name
    val = name[index + 1:]
    if val == 'none':
        val = TARGET_LOST_NONE
    elif val == '0':
        val = TARGET_LOST_ZERO
    else:
        val = TARGET_LOST_DEFAULT
    return val, name[0:index].strip()


def parse_target_name(name):
    index = name.rfind('的')
    if index <= 0:
        return name, TARGET_VALUE_NUMBER
    value_type = get_target_value_type(name[index + 1:])
    if value_type is None:
        return name, TARGET_VALUE_NUMBER
    return name[0:index], value_type


def build_target_item(text, operator, convert_word, lost_word):
    try:
        value = float(text)
        return TargetNumItem(value=value, operator=operator)
    except:
        pass
    lost_type, text = parse_target_lost_type(text)
    text, value_type = parse_target_name(text)
    name, body_type = parse_target_body(text)
    convert_type = convert_target_convert_type(convert_word)
    lost_type = convert_target_lost_type(lost_word)
    item = TargetItem(target_body=body_type, target_name=name, target_value=value_type, lost_type=lost_type,
                      convert_type=convert_type, operator=operator)
    return item
