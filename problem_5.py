from typing import Final, Iterator
from itertools import count

def smallest_multiple() -> int:
    values: Final[Iterator[int]] = count(start=20, step=20)
    divisors: Final[list[int]] = list(range(1, 21))
    for value in values:
        evenly_divisible_by_all_between_1_and_20 = all((
            value % divisor == 0
            for divisor in divisors
        ))
        if evenly_divisible_by_all_between_1_and_20:
            return value

print(smallest_multiple())