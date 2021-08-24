def list_ends(a_list):
    list_1 = []
    if a_list:
        list_1 = [a_list[0], a_list[-1]]
    return list_1

print(list_ends([1,2,3,4,5]))