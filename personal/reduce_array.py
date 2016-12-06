def reduce_array_numbers():
    array = [1, 2, 3, 4, 5]
    reduced = reduce(lambda x, y: x + y, array)
    return reduced


def reduce_array_strings():
    array = ['a', 'b', 'c', 'd', 'e']
    reduced = reduce(lambda x, y: x + y, array)
    return reduced

print reduce_array_numbers()
print reduce_array_strings()
