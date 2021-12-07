def fib(n):
    num1 = 0
    num2 = 1
    for i in range(n):
        sums = num1 + num2
        num1 = num2
        num2 = sums
    return num1

def rec_fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)

def get_list(n):
    return [fib(i) for i in range(1, n + 1)]
    
