### microfone

import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment

from sound_detection import *



def listen():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    seconds_analyze = 0.1  # Duration of recording
    myrecording = None

    while(True):
        analyze_myrecording = sd.rec(int(seconds_analyze * fs), samplerate=fs, channels=2)

        if(analyze_rms(analyze_myrecording, 20)):
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()  # Wait until recording is finished
            print("RECORD")
    return myrecording

if __name__ == "__main__":
    print ("Listening...")
    listen()
    print("End")
