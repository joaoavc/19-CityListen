### microfone

import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import numpy as np
from sound_detection import *


# ruido de fundo 5 minutos
#L95
def listen():
    threshold = calculate_threshold()
    fs = 44100  # Sample rate
    max_time = 10  # Max Duration of recording
    max_samples = fs*max_time
    event_start = False

    while(True):
        if(not event_start):
            event = []
        recording = sd.rec(int(1024), samplerate=fs, channels=2)
        if(analyze_rms(recording, threshold)):
            event.append(recording)
            event_start = True

        size = np.concatenate(event, axis=0 ).shape[0]
        if(size >= max_samples):
            full_event = np.concatenate(event, axis=0)
            print(full_event.shape)
            event_start = False

            


def background_noise():
    print ("Listening background noise...")
    fs = 44100  # Sample rate
    seconds = 300  # Duration of recording
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    return calculate_rms(recording)


def calculate_threshold():
    bcg_noise = background_noise()
    threshold = np.percentile(bcg_noise, 95)
    return threshold


if __name__ == "__main__":
    print ("Listening...")
    listen()
    print("End")
