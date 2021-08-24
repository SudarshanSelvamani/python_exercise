def divisor(number):
    divisors = []
    half_of_number = number // 2 + 1
    for x in range(2, half_of_number):
        if number % x == 0:
            divisors.append(x)
    return divisors

print(divisor(26))
