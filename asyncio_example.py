#!/usr/bin/python3.6
import asyncio
import sys
import time

async def slow_io_func(x):
    print(f"Sending request to website {x + 1}")
    await asyncio.sleep(0.25)
    # while this coroutine sleeps, the scheduler can start other coroutines
    print(f"Got response from website {x + 1}")
    return range(x, 2*x)
    
def data_processing_func(response):
    '''Does the CPU-intensive work of actually processing the website's
     response'''
    return sum(response)
    
def scrape_websites(n = 5):
    '''Simulates sending requests to highx - lowx websites and then processing
the data that was received.'''
    all_scrapers = asyncio.gather(*[slow_io_func(x) for x in range(n)])
    # this starts up all the coroutines, and schedules them for completion
    loop = asyncio.get_event_loop()
    responses = loop.run_until_complete(all_scrapers)
    # in Python 3.7+, we could make this an async function and use
    # asyncio.run(all_scrapers) instead.
    loop.close()
    return [data_processing_func(resp) for resp in responses]
    
if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
    except:
        n = 5
    t0 = time.perf_counter()
    all_sums = scrape_websites(n)
    print(f"Processed results = {all_sums}")
    tf = time.perf_counter() - t0
    print(f"The total time required was {tf/n:.5f} seconds per website.")