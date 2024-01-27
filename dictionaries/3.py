def sum_common_keys(dict1, dict2):
    result = {}
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2[key]
    return result


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(sum_common_keys(dict1, dict2))
