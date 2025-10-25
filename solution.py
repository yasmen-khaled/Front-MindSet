def fibonacci_sum(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return sum(fib)

print(fibonacci_sum(10))
