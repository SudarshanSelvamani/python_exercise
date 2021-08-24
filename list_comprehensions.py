def list_comprehensions(list):
    even_numbers = [x for x in list if x % 2 == 0]
    return even_numbers

print(list_comprehensions([1,2,3,4,5,6,7,8]))