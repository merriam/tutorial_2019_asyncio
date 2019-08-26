#!/usr/bin/env python3
# asyncq.py  -- a queue with producers and consumers handling jobs.

import asyncio
from os import urandom
import time
from random import randint, seed


def make_name(number=0, suffix=""):
    c = [f"\033[{i}m" for i in (0, 31, 32, 33, 34, 35, 36)]
    return f"{c[number % (len(c) - 1) + 1]}{number}{suffix}{c[0]}"


async def make_item(size=5) -> str:
    return urandom(size).hex()  # e.g., 'a6abd91e0f'
    # Docs on urandom are confusing.  It blocks now?


async def rand_sleep(min_secs=1, max_secs=5, caller="") -> None:
    i = randint(min_secs, max_secs)
    print(f"{caller}:rand_sleep:  sleeping for {i} seconds")
    await asyncio.sleep(i)


async def produce(number, q: asyncio.Queue) -> None:
    name = make_name(number, "/prod")
    for count in range(number):
        print(f"{name}:starting")
        await rand_sleep(caller=name)
        print(f"{name}:make_item:start ({count} of {number})")
        item = await make_item()
        print(f"{name}:make_item:end ({item})")
        t = time.perf_counter()
        await q.put((item, t))
        print(f"{name}: added {item} to queue ({count} of {number})")
    print(f"{name} Completed Producing All Jobs")


async def consume(number: int, q: asyncio.Queue) -> None:
    name = make_name(number, "/cons")
    while True:
        print(f"{name}:starting")
        t_wait = time.perf_counter()
        item, t = await q.get()
        print(f"{name}:got item {item} after {time.perf_counter()-t_wait:0.5f} idle, "
             f"delayed {time.perf_counter() - t:0.5f} seconds. {q.qsize()} in Queue")
        await rand_sleep(caller=name)
        now = time.perf_counter()
        print(f"{name}: Completed element {item} in {now - t:0.5f} seconds.")
        q.task_done()


async def main(nprod: int, ncon: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers)  # just wait until all producers are done
    await q.join()  # Implicitly awaits consumers, too, until all q.task_done() are called
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    seed(444)
    producers, consumers = 9, 2
    start = time.perf_counter()
    asyncio.run(main(producers, consumers))
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds. {producers} producers and {consumers} consumers")
