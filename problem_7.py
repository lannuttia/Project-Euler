import heapq
from itertools import count, islice
from dataclasses import dataclass, field


def primes():
    @dataclass(init=True, order=True)
    class Element:
        key: int = field(compare=True)
        nums: any = field(compare=False)

    yield 2
    queue = [Element(4, count(8, 4))]
    numbers = count(3, 2)
    for number in numbers:
        prev_min = None
        while queue[0].key <= number:
            cur_min = queue[0]
            prev_min = heapq.heappushpop(
                queue,
                Element(next(cur_min.nums), cur_min.nums)
            )
        if not prev_min or prev_min.key != number:
            num_sq = number ** 2
            heapq.heappush(
                queue,
                Element(num_sq, count(num_sq + 2 * number, 2 * number))
            )
            yield number

print(list(islice(primes(), 10001))[-1])