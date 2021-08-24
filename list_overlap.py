def list_overlap(list_1, list_2):
    unique_number_list_1 = list(set(list_1))
    unique_number_list_2 = list(set(list_2))
    common_numbers= []
    for number in unique_number_list_1:
        if number in unique_number_list_2:
            common_numbers.append(number)
    
    return common_numbers

print(list_overlap([1,2,3],[2,3,3,3,3,3,3,3]))



