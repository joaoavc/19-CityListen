### microfone

import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment

from sound_detection import *



def listen():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    return myrecording

if __name__ == "__main__":
    print ("Listening...")
    listen()
    print("End")
