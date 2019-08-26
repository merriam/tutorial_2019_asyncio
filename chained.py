#!/usr/bin/env python3
# chained.py
import asyncio
from random import randint
import time

c = ("\033[0m",  # End of color
     "\033[36m",  # cyan (0x24)
     "\033[91m",  # red (0x8A)
     "\033[35m")  # Magenta (0x23)


async def part1(n) -> str:
    i = randint(0, 10)
    print(f"{n}: part1: sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-part1"
    print(f"{n}: part1: returning {result}")
    return result  # calling part1() returns a coroutine, running the coroutine returns this.


async def part2(n, part1_result) -> str:
    i = randint(0, 10)
    print(f"{n}: part2: sleeping for {1} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-part2 derived from {part1_result}"
    print(f"{n}: part2: returning {result}")
    return result  # calling part1() returns a coroutine, running the coroutine returns this.


async def chain(n):
    start = time.perf_counter()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    end = time.perf_counter() - start
    print(f"{n}: chained result took {end} seconds, returned {p2}")


async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))


if __name__ == "__main__":
    args = [f"{c[i % 3 + 1]}{i}{c[0]}" for i in range(5)]
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")
