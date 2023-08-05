def get_items_type_name(value, items):
    for item in items:
        if item['value'] == value:
            return item['name']
    return ""


def get_target_value_type0(name, items):
    for item in items:
        if item['name'] == name:
            return item['value']
    return None
