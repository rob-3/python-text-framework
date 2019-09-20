def find(arr, function):
    for item in arr:
        if function(item):
            return item
    return None
