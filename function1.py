import asyncio

async def fn1():
    print("start function 1")
    await asyncio.sleep(2)
    print("end function 1")

async def fn2():
    print("start function 2")
    await asyncio.sleep(1)
    print("end function 2")

async def main():
    task1 = asyncio.create_task(fn1())
    task2 = asyncio.create_task(fn2())

    await task1
    await task2

asyncio.run(main())
