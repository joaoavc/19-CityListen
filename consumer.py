from threading import Thread
from pyring    import LockedRingBuffer 

import time

from sound_detection import *
from classifier      import *


# Producer Thread Class
class EventAnalysis(Thread):
    
    def __init__(self, buffer, empty, full):
        super().__init__()
        self.buffer = buffer
        self.empty = empty
        self.full = full

    def run(self):
        counter = 0
        out_index = 0
        while True:
            self.full.acquire()
            sequence, value = self.buffer.get(out_index)
            out_index = out_index + 1

            features = sound_features(value)
            classification = classifier(features)
            
            counter +=1
            print("Events Analyzed: ", sequence+1, " |||  Classification:", classification[0])
            self.empty.release()
                   


