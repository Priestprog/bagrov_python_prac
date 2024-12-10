import asyncio

async def squere(x):
    return x*x

async def doubler(x):
    return x*2


async def main(x,y):
    dx,dy = await asyncio.gather(doubler(x), doubler(y))
    dx, dy = await asyncio.gather(squere(dx), squere(dy))
    return dx, dy



print(*asyncio.run(main(2,3)))