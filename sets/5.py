def set_difference_symmetric(set1, set2):
    difference = set1 - set2
    symmetric_difference = set1 ^ set2
    return difference, symmetric_difference


set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "kiwi", "orange"}
print(*set_difference_symmetric(set1, set2))
