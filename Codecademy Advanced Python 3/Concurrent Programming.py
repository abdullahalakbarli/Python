"""
📌 Kısa Açıklamalar: Concurrent Programming in Python

1️⃣ **Thread (İş Parçacığı):**  
   - Aynı süreç (process) içinde çalışan, bağımsız yürütülebilen en küçük işlem birimidir.
   - `threading` modülü ile oluşturulur ve özellikle I/O-bound işlemler için uygundur.  

2️⃣ Multiple Threads (Çoklu İş Parçacıkları): 
   - Aynı anda birden fazla thread çalıştırarak işleri eşzamanlı (concurrent) yürütmeyi sağlar.
   - Paralellik (gerçek eşzamanlılık) sağlamaz, ancak işlemleri hızlandırabilir.  

3️⃣ Async/Await (Asenkron Programlama):
   - `asyncio` modülü ile kullanılır, tek bir thread içinde çok sayıda işlemi eşzamanlı çalıştırır.
   - Özellikle ağ istekleri (API çağrıları), dosya okuma/yazma ve veritabanı sorguları gibi I/O-bound işlemler için en verimli çözümdür.

4️⃣ Process (Süreç):
   - İşletim sistemi tarafından bağımsız olarak çalıştırılan bir program örneğidir. 
   - `multiprocessing` modülü ile oluşturulabilir ve CPU-bound (yoğun işlem gücü gerektiren) işlemler için idealdir, çünkü GIL sınırlamasını aşar.

🚀 Özet:  
✔ I/O bound işlemler için:** Threading veya Async/Await kullanılır.  
✔ CPU bound işlemler için: Multiprocessing kullanılır."""

import time
import threading
import asyncio
from multiprocessing import Process


def cal_average(num): 
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  time.sleep(1)
  return avg

def main_sequential(list1, list2, list3): 
  s = time.perf_counter()
  print(cal_average(list1))
  print(cal_average(list2))
  print(cal_average(list3))
  elapsed = time.perf_counter() - s
  print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")

async def cal_average_async(num): 
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  await asyncio.sleep(1)
  return avg

async def main_async(list1, list2, list3): 
  s = time.perf_counter()
  tasks = [cal_average_async(list1), cal_average_async(list2), cal_average_async(list3)]
  await asyncio.gather(*tasks)
  elapsed = time.perf_counter() - s
  print("Asynchronous Programming Elapsed Time: " + str(elapsed) + " seconds")

def main_threading(list1, list2, list3):
  s = time.perf_counter()
  lists = [list1, list2, list3]
  threads = []
  for num in range(len(lists)):
    x = threading.Thread(target = cal_average, args =(lists[num],))
    threads.append(x)
    x.start()
  for t in threads:
    t.join()
  elapsed = time.perf_counter() - s
  print("Threading Elapsed Time: " + str(elapsed) + " seconds")

def main_multiprocessing(list1, list2, list3): 
  s = time.perf_counter()
  lists = [list1, list2, list3]
  procesess = [Process(target=cal_average, args=(lists[x],)) for x in range(len(lists))]
  for p in procesess:
    p.start()
  elapsed = time.perf_counter() - s
  print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")


if __name__ == '__main__':
  l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
  l2 = [2, 4, 6, 8, 10]
  l3 = [1, 3, 5, 7, 9, 11]
  main_sequential(l1, l2, l3)
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main_async(l1, l2, l3))
  main_threading(l1, l2, l3)
  main_multiprocessing(l1, l2, l3)
