def list_less_than_ten(number_list):
    number_list_less_than_5 = [ x for x in number_list if x < 5]
    return number_list_less_than_5

print(list_less_than_ten([2,3,4,5,6,7,8]))