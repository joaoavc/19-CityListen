### main ###

from microfone       import *
from classifier      import *
from sound_detection import *

if __name__ == "__main__":
    print (" ## Listening... ##")
    listen_audio()
    split_sound()
    print("## Sound recorded ##")
    print("--------------------------------------------------------------------------")
    print("## Extracting features... ##")
    features = sound_features()
    print("## Features extracted... ##")
    print("--------------------------------------------------------------------------")
    print("## Classifying...")
    classification = classifier(features)
    print("Prediction: ", classification)
    print("--------------------------------------------------------------------------")


    

