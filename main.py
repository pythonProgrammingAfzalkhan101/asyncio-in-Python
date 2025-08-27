import asyncio  

async def task_one():
    print("Task one is stared")
    await asyncio.sleep(2)
    print("Task one is end")

async def task_two():
    print("Task Two is started")
    await asyncio.sleep(1)
    print("Task two is end")

async def main():
    await asyncio.gather(task_one(),task_two())

asyncio.run(main())
