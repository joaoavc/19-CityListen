import threading
import time
from pyring    import LockedRingBuffer 


# Shared Memory variables
CAPACITY = 10
buffer = [-1 for i in range(CAPACITY)]
in_index = 0
out_index = 0
 
# Declaring Semaphores
mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)

REAL_BUFFER = LockedRingBuffer(CAPACITY) 
 
# Producer Thread Class
class Producer(threading.Thread):
  def run(self):
     
    global CAPACITY, buffer, in_index, out_index
    global mutex, empty, full
     
    items_produced = 0
    counter = 0
     
    while items_produced < 20:
      empty.acquire()
      #mutex.acquire()
       
      counter += 1
      REAL_BUFFER.put(counter)
      
      #buffer[in_index] = counter
      #in_index = (in_index + 1)%CAPACITY
      time.sleep(3)
      print("Producer produced : ", counter)
       
      #mutex.release()
      full.release()
       
      time.sleep(1)
       
      items_produced += 1
 
# Consumer Thread Class
class Consumer(threading.Thread):
  def run(self):
     
    global CAPACITY, buffer, in_index, out_index, counter
    global mutex, empty, full
     
    items_consumed = 0
     
    while items_consumed < 20:
      full.acquire()
      #mutex.acquire()
       
      sequence, value = REAL_BUFFER.get(out_index)
      out_index = out_index + 1
      time.sleep(0.3)
      print("Consumer consumed item : ", value)
       
      #mutex.release()
      empty.release()      
              
      items_consumed += 1
 
# Creating Threads
producer = Producer()
consumer = Consumer()
 
# Starting Threads
consumer.start()
producer.start()
 
# Waiting for threads to complete
producer.join()
consumer.join()
