#!/usr/bin/env python3
# countasync.py

import asyncio
import time

async def f(x):
    y = await f(x)  # OK - `await` and `return` allowed in coroutines
    # and f() must be 'awaitable' being a coroutine or implementing __await__()
    # but "yield from z()" is not allowed
    return y

async def g(x):
    yield x  # OK - this is an async generator


async def count(name=""):
    """ native coroutine, modern syntax """
    print(f"One {name}")
    await asyncio.sleep(1)  # must be 'awaitable', a coroutine or having __await__
    print(f"Two {name}")
    return f"{name} completed"

@asyncio.coroutine
def count_co(name=""):
    """Generator-based coroutine, older syntax.  Going in Python 3.10. """
    print(f"One {name}")
    yield from asyncio.sleep(1)  # "yield from" instead of "await" because older syntax
    print(f"Two {name}")
    return f"{name} completed"

async def main():
    x = count("x")  # does nothing but make a new coroutine object.  No autostart.
    rets = await asyncio.gather(count('a'), count('b'), count('c'), count_co('d'), count_co('e'), x)
    # this returns a coroutine object
    print("async return return values: ", rets)
    return "THIS VALUE RETURNED BY asyncio.run"

if __name__ == "__main__":
    # note that "await counter()" not allowed because this is not a 'async def' / awaitable
    s = time.perf_counter()
    r = asyncio.run(main())
    print(r)
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
