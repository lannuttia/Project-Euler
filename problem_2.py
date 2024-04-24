from typing import Iterator
from itertools import takewhile

def fibonacci() -> Iterator[int]:
    previous = 0
    current = 1
    yield previous
    yield current
    while True:
        current, previous = previous + current, current
        yield current
        
infinite_fib_numbers = fibonacci()
fib_numbers_less_than_4_million = takewhile(lambda num: num <= 4000000, infinite_fib_numbers)
even_fib_numbers_less_than_4_million = (num for num in fib_numbers_less_than_4_million if num % 2 == 0)
print(sum(even_fib_numbers_less_than_4_million))