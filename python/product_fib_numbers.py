
from functools import lru_cache

@lru_cache
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

def productFib(prod):
    index = 0

    while fibonacci(index) * fibonacci(index+1) < prod:
        index += 1

    return [
        fibonacci(index),
        fibonacci(index+1),
        fibonacci(index)*fibonacci(index+1) == prod
    ]



assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5

assert productFib(4895) == [55, 89, True]
assert productFib(5895) == [89, 144, False]
