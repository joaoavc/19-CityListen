### main ###

from threading import Thread, Semaphore
from pyring    import LockedRingBuffer 
import time

from microfone       import *
from classifier      import *
from sound_detection import *
from producer        import *
from consumer        import *

# Shared Memory variables
CAPACITY = 120
buffer = LockedRingBuffer()
in_index = 0
out_index = 0
 
# Declaring Semaphores
mutex = Semaphore()
empty = Semaphore(CAPACITY)
full = Semaphore(0)

# Creating Threads
producer = SoundCapture(buffer, empty, full)
consumer = EventAnalysis(buffer, empty, full)
 
# Starting Threads
producer.start()
consumer.start()

# Waiting for threads to complete
producer.join()
consumer.join()


##if __name__ == "__main__":
##
##
##    while(True):
##    
##        print (" ## Listening... ##")
##        sound_record  = listen()
##        start_time = time.time()
##        print("## Sound recorded ##")
##        print("--------------------------------------------------------------------------")
##        print("## Extracting features... ##")
##        features = sound_features(sound_record)
##        print("## Features extracted... ##")
##        print("--------------------------------------------------------------------------")
##        print("## Classifying...")
##        classification = classifier(features)
##        print("Prediction: ", classification)
##        print("--- %s seconds ---" % (time.time() - start_time))
##        print("--------------------------------------------------------------------------")
##        print("--------------------------------------------------------------------------")
##        print("--------------------------------------------------------------------------")
##        print('\n')
##        
##
#### em real time
##
