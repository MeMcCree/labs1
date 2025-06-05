def integers_only(lst):
    filtered = [x for x in lst if type(x) is int]
    filtered.sort()
    return filtered