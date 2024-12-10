import asyncio

async def squere(x):
    return x*x

async def doubler(x):
    return x*2


async def main(x,y):
    async with asyncio.TaskGroup() as tg:
        task = tg.create_task(doubler(x)), tg.create_task(doubler(y))
    dx,dy = task[0].result(), task[1].result()
    async with asyncio.TaskGroup() as tg:
        task = tg.create_task(squere(dx)), tg.create_task(squere(dy))
    dx,dy = task[0].result(), task[1].result()
    return dx, dy



print(*asyncio.run(main(2,3)))