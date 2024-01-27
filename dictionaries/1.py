def sort_dict_values(input_dict):
    return {key: sorted(value) for key, value in input_dict.items()}


dictionary = {"a": [3, 1, 2], "b": [5, 4, 6], "c": [8, 7, 9]}
print(sort_dict_values(dictionary))
