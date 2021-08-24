def string_lists(string):
    half_length_of_string = int(len(string)/2)
    palindrome_check = False
    if len(string) % 2 == 0:
        if string[:half_length_of_string] == string[:half_length_of_string-1:-1]:
            palindrome_check = True
    else:        
        if string[:half_length_of_string] == string[:half_length_of_string:-1]:
            palindrome_check = True
    
    if palindrome_check:
        print('Given string is a palindrome')
    else:
        print('Given String is not a palindrome')

string_lists('1441')
string_lists('madam')
string_lists('list')
string_lists('laser')
        