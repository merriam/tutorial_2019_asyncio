#!/usr/bin/env python3
# rand.py

import asyncio
import random

# ANSI colors
c = ("\033[0m",  # End of color
     "\033[36m",  # cyan (0x24)
     "\033[91m",  # red (0x8A)
     "\033[35m")  # Magenta (0x23)


async def make_random(threshold: int = 6, number=0) -> int:
    n = f"{c[1 + number % 3]}{number}{c[0]}"
    print(f"{n}:  Initiated, threshold= {threshold}")
    i = random.randint(0, 10)
    while i <= threshold:
        print(f"{n}:  too low; retrying; sleeping {number}")
        await asyncio.sleep(number)  # mimic an IO bound process
        i = random.randint(0, 10)
    print(f"{n}:  finished, with {i}")
    return i


async def main():
    res = await asyncio.gather(*(make_random(random.randint(5, 10), i) for i in range(9)))
    return res


if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
