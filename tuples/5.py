def sort_tuples_by_int(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1], reverse=True)


tuples_list = [("apple", 2), ("banana", 3), ("cherry", 1)]
print(sort_tuples_by_int(tuples_list))
