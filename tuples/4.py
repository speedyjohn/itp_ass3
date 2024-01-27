def separate_tuple_elements(tuples_list):
    list1 = [item[0] for item in tuples_list]
    list2 = [item[1] for item in tuples_list]
    list3 = [item[2] for item in tuples_list]
    return list1, list2, list3


tuples_list = [(1, 'a', 'apple'), (2, 'b', 'banana'), (3, 'c', 'cherry')]
print(separate_tuple_elements(tuples_list))
