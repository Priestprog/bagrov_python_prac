import asyncio
from asyncio import Queue

async def writer(queue, delay, stop_event, prefix):
    counter = 0
    await asyncio.sleep(delay)
    while not stop_event.is_set():
        await queue.put((counter, f"{counter}_{prefix}"))
        counter += 1
        await asyncio.sleep(delay)

async def stacker(queue, stack, stop_event):
    while not stop_event.is_set() or not queue.empty():
        if not queue.empty():
            _, item = await queue.get()
            stack.append(item)
        else:
            await asyncio.sleep(0.1)

async def reader(stack, count, delay, stop_event):
    await asyncio.sleep(delay)
    for _ in range(count):
        while not stack:
            await asyncio.sleep(0.1)
        print(stack.pop(0))
        await asyncio.sleep(delay)
    stop_event.set()

async def main():
    delay1, delay2, delay3, count = map(int, input().split(","))

    queue = Queue()
    stack = []
    stop_event = asyncio.Event()

    writer1 = writer(queue, delay1, stop_event, delay1)
    writer2 = writer(queue, delay2, stop_event, delay2)
    stacker_task = stacker(queue, stack, stop_event)
    reader_task = reader(stack, count, delay3, stop_event)

    await asyncio.gather(writer1, writer2, stacker_task, reader_task)

asyncio.run(main())
