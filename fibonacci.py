def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def print_fibonacci(n):
    for i in range(0,n):
        print(fibonacci(i))

print_fibonacci(10)
    