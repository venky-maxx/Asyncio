import asyncio
a=0
async def send_data():
    print("Sending data to the data base is intiated...")
    await asyncio.sleep(2)
    print("Data sent to database successfully")
    a= 10

async def verify(a):
    print(a)

async def my_work_flow():
    print("Processing the data....")
    task = asyncio.create_task(send_data())
    await asyncio.sleep(4)
    print('work completed')
    

asyncio.run(my_work_flow())
asyncio.run(verify(a))
