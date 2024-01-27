def common_elements(list_1, list_2):
    return sorted(set(list_1) & set(list_2))


list_1 = [1, 2, 3, 4, 5, 5, 6]
list_2 = [4, 5, 6, 7, 8]
print(common_elements(list_1, list_2))
