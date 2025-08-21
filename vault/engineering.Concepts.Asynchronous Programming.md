---
id: y660ulvr06vgpnb52e5b2ig
title: Asynchronous Programming
desc: ''
updated: 1755761908315
created: 1755761895909
---
```python
import asyncio
import time

async def five_sec():
    """
    Test asyncio.as_completed
    this takes 5 seconds to complete
    """
    t1 = asyncio.sleep(5,'5sec')
    t2 = asyncio.sleep(2,'2sec')
    for t in asyncio.as_completed([t1,t2]):
        print(await t)

async def one_sec():
    """
    Test asyncio.as_completed
    this takes 1 second to complete
    """
    print(await asyncio.sleep(1,'1sec'))


async def six_sec():
    print(await one_sec())
    print(await five_sec())

async def five_sec_and_one_sec():
    """
    Test asyncio.gather
    this takes 5 seconds to complete
    """
    await asyncio.gather(one_sec(), five_sec())

def create_one_sec_task():
    """
    Test asyncio.create_task
    this takes 1 second to complete
    """
    return asyncio.create_task(one_sec())

def create_five_sec_task():
    """
    Test asyncio.create_task
    this takes 5 seconds to complete
    """
    return asyncio.create_task(five_sec())

async def main_five_sec_total():
    """
    Test asyncio.gather
    this takes 5 seconds to complete
    """
    t2 = create_one_sec_task()
    t1 = create_five_sec_task()
    await t2
    await t1
    
async def producer(queue: asyncio.Queue):
    for i in range(5):
        print(f"Producer putting {i}")
        await queue.put(i)
        await asyncio.sleep(0.5)  # simulate work

    await queue.put(None)  # Sentinel to tell the consumer to finish

async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:
            print("Consumer got sentinel, exiting.")
            break
        print(f"Consumer got {item}")
        await asyncio.sleep(1)  # simulate processing

async def main_queue():
    queue = asyncio.Queue()
    await asyncio.gather(
        producer(queue),
        consumer(queue)
    )


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Time taken: {end - start} seconds")

```