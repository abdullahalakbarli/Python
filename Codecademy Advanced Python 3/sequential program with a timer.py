import time
def sequential():
  s = time.perf_counter()
  print("Abdullah")
  time.sleep(2)
  print("says hello!")
  elapsed = time.perf_counter() - s
  print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")

sequential()
