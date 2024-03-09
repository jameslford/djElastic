from typing import List


def unflatten(data: dict, field_names: List[str], field_options: dict):
    """
    This will be used to unflatten the data
    """
    if len(field_names) == 1:
        data[field_names[0]] = field_options
    else:
        field_name = field_names.pop(0)
        if field_name not in data:
            data[field_name] = {}
        unflatten(data[field_name], field_names, field_options)
