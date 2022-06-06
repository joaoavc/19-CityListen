# microfone

import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import numpy as np
from sound_detection import *


# ruido de fundo 5 minutos
# L95
def listen():
    # testar real audio 
    audioname = "yell.wav"
    y, sr = librosa.load(audioname, mono=True)

    threshold = calculate_threshold()
    fs = 44100  # Sample rate
    max_time = 10  # Max Duration of recording
    max_samples = fs*max_time
    event_start = False
    event_end = False

    # while(True):
    if(not event_start): event = []
    #recording = sd.rec(int(1024), samplerate=fs, channels=2)
    #sd.wait()  # Wait until recording is finished
    #is_event = analyze_rms(recording, threshold)

    is_event = analyze_rms(y, threshold)
    print("IS EVENT:", is_event)

    if(is_event):
        event.append(y)
        event_start = True
        event_end = True # testar
    elif(not is_event and event_start): event_end = True

    size = np.concatenate(event, axis=0)
    print(size.shape)
    if(len(event) != 0): size = size.shape[0]
    else: size = 0

    if(size >= max_samples or event_end):
        full_event = np.concatenate(event, axis=0)
        print("SIZE EVENT: ", full_event.shape)
        event_start = False


def background_noise():
    print("Listening background noise...")
    fs = 44100  # Sample rate
    seconds = 5  # Duration of recording
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    return calculate_rms(recording)


def calculate_threshold():
    bcg_noise = background_noise()
    threshold = np.percentile(bcg_noise, 95)
    print("Threshold: ", threshold)
    return threshold


if __name__ == "__main__":
    print("Listening...")
    listen()
    print("End")
