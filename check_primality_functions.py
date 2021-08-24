def check_primality_functions():
    number = get_integer('Enter a number: ')
    for i in range(2,(number//2)+1):
        if number % i == 0:
            print("Number is not a prime")
            return
    print("Number is a prime number")





def get_integer(help_text):
    return int(input(help_text))

check_primality_functions()