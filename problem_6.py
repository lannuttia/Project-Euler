from typing import Final, Iterator

def sum_of_squares(max: int) -> int:
    values: Final[Iterator[int]] = range(1, max + 1)
    return sum((pow(value, 2) for value in values))
    
def square_of_sums(max: int) -> int:
    values: Final[Iterator[int]] = range(1, max + 1)
    return pow(sum(values), 2)

def sum_square_difference(max: int) -> int:
    return square_of_sums(max) - sum_of_squares(max)

print(sum_square_difference(100))