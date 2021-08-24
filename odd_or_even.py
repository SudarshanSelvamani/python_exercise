def odd_or_even():
    number = int(input("Enter a interger"))
    if number % 2 == 0:
        print('Its a even number')
        if number % 4 == 0:
            print('The number is also divisible by 4')
    else:
        print('Number is a odd number')

odd_or_even()