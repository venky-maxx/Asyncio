import asyncio

async def function():
    return "Testing"

async def hru():
    return "Testing"

async def fetch():
    return "Testing"
   
async def parallel():
    return await asyncio.gather(function(), hru(), fetch())

print(asyncio.run(parallel()))