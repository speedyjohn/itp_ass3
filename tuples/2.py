def common_elements_tuple(tuple1, tuple2):
    return tuple(element for element in tuple1 if element in tuple2)


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 5, 7, 9)
print(common_elements_tuple(tuple1, tuple2))
