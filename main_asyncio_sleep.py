import asyncio

async def function():
    await asyncio.sleep(5)
    return "Testing"

async def hru():
    return "Testing"

async def fetch():
    return "Testing"
   
async def parallel():
    return await asyncio.gather(function(), hru(), fetch())

print(asyncio.run(parallel()))