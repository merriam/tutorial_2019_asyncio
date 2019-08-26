# Async IO Tutorial
From https://realpython.com/async-io-python/

** Made these programs:
* countasync.py - Basic interleaved sleeping and counting with decorators and experiments.
* chained.py - Simple pattern of gathering calls each calling a sequential pair of slow async functions.asyncs calling asyncs.
* rand.py - # rand.py - Gather a set of task that have random retry times to complete.
* asyncq.py - a queue with producers and consumers handling jobs.
* areq.py - Gather URLs from web pages listed in `urls.txt`, write into `foundurls.txt`.

There is more I could do:

* Recurse `areq.py` using `aioreddis` to make a 'broken link finder'.
* Play with `curio` and `trio` to understand their takes on asyncio.
* Go off and play with more threading, event driven, or multiprocessor stuff.

Done for now.