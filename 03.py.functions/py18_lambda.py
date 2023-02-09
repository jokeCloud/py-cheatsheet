from functools import reduce

n = 3
factorial = reduce(lambda x, y: x*y, range(1, n+1))
print(factorial)


def fib(n): return n if n <= 1 else fib(n-1) + fib(n-2)


result = fib(10)
print(result)
