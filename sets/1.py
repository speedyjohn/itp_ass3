def set_operations(set1, set2):
    union_set = set1 | set2
    intersection_set = set1 & set2
    difference_set = set1 - set2
    return union_set, intersection_set, difference_set


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(*set_operations(set1, set2))
