def list_remove_duplicates_using_set(a_list):
    return list(set(a_list))

print(list_remove_duplicates_using_set([1,1,1,1,1,2,2,2]))

def list_remove_duplicates_using_loop(a_list):
    another_list = []
    for element in a_list:
        if element not in another_list:
            another_list.append(element)
    return another_list

print(list_remove_duplicates_using_loop([1,1,1,1,1,2,2]))


