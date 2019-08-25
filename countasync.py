#!/usr/bin/env python3
# countasync.py

import asyncio
import time

async def count(name=""):
    print(f"One {name}")
    await asyncio.sleep(1)
    print(f"Two {name}")
    return f"{name} completed"

@asyncio.coroutine
async def count_co(name=""):
    print(f"One {name}")
    await asyncio.sleep(1)
    print(f"Two {name}")
    return f"{name} completed"

async def main():
    x = count("x")  # does nothing but make a new coroutine object.  No autostart.
    rets = await asyncio.gather(count('a'), count('b'), count('c'), count_co('d'), count_co('e'), x)
    # this returns a coroutine object
    print("async return return values: ", rets)
    return "THIS VALUE RETURNED BY asyncio.run"

if __name__ == "__main__":
    s = time.perf_counter()
    r = asyncio.run(main())
    print(r)
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
