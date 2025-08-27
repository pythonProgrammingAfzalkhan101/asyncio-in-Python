import asyncio
async def say_hello():

    print("হ্যালো...")
    await asyncio.sleep(2)
    print("কেমন আছো?")

async def main():
    
    await say_hello()

asyncio.run(main())
