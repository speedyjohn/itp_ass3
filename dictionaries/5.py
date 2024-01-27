def sort_dict_by_values(d):
    sorted_tuples = sorted(d.items(), key=lambda item: item[1], reverse=True)

    return sorted_tuples


example_dict = {'apple': 10, 'banana': 5, 'cherry': 15, 'date': 2}
print(sort_dict_by_values(example_dict))
