def reverse_in_groups(lst, k):
    result = []
    for i in range(0, len(lst), k):
        result.extend(lst[i:i + k][::-1])
    return result


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(reverse_in_groups(lst, k))
