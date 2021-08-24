def list_overlap_comprehension(list_1, list_2):
    unique_number_list_1 = list(set(list_1))
    unique_number_list_2 = list(set(list_2))
    return [x for x in unique_number_list_1 if x in unique_number_list_2]

print(list_overlap_comprehension([1,2,3],[2,3,3,3,3,3,3,3]))