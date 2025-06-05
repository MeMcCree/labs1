def typification(data):
    type_dict = {
        'int': [],
        'str': [],
        'float': [],
        'tuple': [],
        'list': [],
        'dict': [],
        'bool': [],
        'set': []
    }
    
    for item in data:
        item_type = type(item).__name__
        if item_type in type_dict:
            type_dict[item_type].append(item)
    
    result = {k: v for k, v in type_dict.items() if v}
    return result