def common_elements_and_subsets(sets_list):
    common_elements = set.intersection(*sets_list)
    subset_found = False
    for i in sets_list:
        for j in sets_list:
            if i < j or j < i:
                subset_found = True
                print(i, j)
        if subset_found: break


    return common_elements, subset_found


sets_list = [{1, 2, 3}, {2, 3, 4}, {2, 3}]
print(*common_elements_and_subsets(sets_list))
