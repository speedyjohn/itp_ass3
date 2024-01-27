def merge_alternate(list_1, list_2):
    merged_list = []
    len1, len2 = len(list_1), len(list_2)
    for i in range(max(len1, len2)):
        if i < len1:
            merged_list.append(list_1[i])
        if i < len2:
            merged_list.append(list_2[i])

    return merged_list


list1 = [1, 3, 5]
list2 = [2, 4, 6, 8, 10]

print(merge_alternate(list1, list2))
