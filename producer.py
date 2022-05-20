from pyring    import LockedRingBuffer 
from threading import Thread
import time


from microfone       import *
from sound_detection import *


# Producer Thread Class
class SoundCapture(Thread):
    
    def __init__(self, buffer, empty, full):
        super().__init__()
        self.buffer = buffer
        self.full = full
        self.empty = empty

    def run(self):
        counter = 0
        while True:
            self.empty.acquire()           
            sound_record  = listen()
            self.buffer.put(sound_record)
            counter +=1
            print("Sound Captured:  ", counter)
            self.full.release()
                   
