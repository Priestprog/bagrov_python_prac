import asyncio
async def prod(queue, val):
    for i in range(5):
        await queue.put(f"{val}_{i}")
        print(f"Producing {val}_{i} to q1")
        await asyncio.sleep(1)

async def mid(queue1, queue2):
    while True:
        res = await queue1.get()
        print(f"Consuming {res} from q1")
        await queue2.put(res)
        print(f"Puting {res} to q2")

async def cons(queue):
    while True:
        res = await queue.get()
        print(f"Consuming {res} from q2")

async def main():
    queue1, queue2 = asyncio.Queue(), asyncio.Queue()
    await asyncio.gather(
        prod(queue1, 12),
        mid(queue1, queue2),
        cons(queue2),
        cons(queue2))

asyncio.run(main())