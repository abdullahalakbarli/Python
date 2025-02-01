import time
import asyncio

async def greeting_with_sleep_async(string):
  s = time.perf_counter()
  print(string)
  await asyncio.sleep(2)
  print("says hello!")
  elapsed = time.perf_counter() - s
  print("Asyncio Elapsed Time: " + str(elapsed) + " seconds")

loop = asyncio.get_event_loop()
loop.run_until_complete(greeting_with_sleep_async('Codecademy'))
