import asyncio

async def wait(name,ev, evname):
    await ev.wait()
    print(name, "received",evname)


async def send(name, ev, evname):
    ev.set()
    print(name,"generated", evname)

async def snd(ev):

    await send("snd", ev, "evsnd")

async def mid(num,evw,evs):
    await wait("mid", evw, "evsnd")
    await send("mid", evs, "evmid")

async def rcv(ev0,ev1):
    await wait("rcv", ev0, "evmid0")
    await wait("rcv", ev1, "evsnd1")



async def main():
    evs,evm0, enm1= asyncio.Event(), asyncio.Event(), asyncio.Event()
    res = await asyncio.gather(snd(evs), mid(0,evs,evm0),mid(1,evs,evm0), rcv(evm0,enm1))
    return res

asyncio.run(main())
