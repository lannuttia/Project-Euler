from typing import Final, Iterator
from itertools import count, takewhile

def palindroms_from_product_of_3_digit_numbers() -> Iterator[int]:
    first: Final[Iterator[int]] = range(999, 99, -1)
    for i in first:
        second: Iterator[int] = range(999, 99, -1)
        for j in second:
            product: int = i * j
            if str(product) == str(product)[::-1]:
                yield product


print(max(palindroms_from_product_of_3_digit_numbers()))