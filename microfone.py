# microfone


import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import numpy as np
from sound_detection import *


fs = 44100  # Sample rate
max_time = 10  # Max Duration of recording
max_samples = fs*max_time
delta_on = 10
delta_off = 10


# ruido de fundo 5 minutos
# L95
# join sepctrual flux with rms
# delta on
# delta off

def event_detection():
    audioname = "SonsTeste_SNR60 Mixdown_Cidade1.wav"      # testar real audio 
    y, sr = librosa.load(audioname, mono=True)
    threshold = calculate_threshold()
    event_start = False
    event_end = False
    timer_on = 0
    timer_off = 0

    while(True):
        if(not event_start): event = []
        recording = sd.rec(int(1024), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished

        is_on = analyze_rms(recording, threshold)
        flux = analyze_spectrual_flux(recording, threshold)
        if(is_on): print("IS EVENT:", is_on)

        if((is_on or flux) and not event_start):
            event.append(y)
            on(recording, threshold, timer_on)
            global delta_on
            if(timer_on == delta_on): event_start = True

        elif(not is_on and event_start):
            event.append(recording)
            off(y, threshold, timer_on)
            global delta_off
            if(timer_off == delta_off): event_end = True

        # event_end = True # testar
        elif(is_on and event_start): event.append(recording)

     
        if(len(event) != 0): size = size.shape[0]
        else: size = 0

        if(size >= max_samples or event_end):
            full_event = np.concatenate(event, axis=0)
            print("SIZE EVENT: ", full_event.shape)
            event_start = False
            event_end = False

    #return full_event

def background_noise():
    print("Listening background noise...")
    fs = 44100  # Sample rate
    seconds = 5  # Duration of recording
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    return calculate_rms(recording)


def event_detection_file_test():
    audioname = "SonsTeste_SNR60 Mixdown_Cidade1.wav"      # testar real audio 
    y, sr = librosa.load(audioname, mono=True)



    threshold = calculate_threshold()
    event_start = False
    event_end = False
    timer_on = 0
    timer_off = 0
    last_ind = 0
    next_ind = 1024
    is_on=False
    for i in range(0, len(y), 1024):
        if(len(y)-next_ind<1024): break
        if(not event_start and not is_on): event = []

        sample = y[last_ind:next_ind]
        
        is_on = analyze_rms(sample, threshold)
        flux = analyze_spectrual_flux(sample, threshold)

        if((is_on or flux) and not event_start):
            event.append(sample)
            timer_on = on(sample, threshold, timer_on)
            global delta_on
            if(timer_on == delta_on): event_start = True

        elif(not is_on and event_start):
            event.append(sample)
            timer_off = off(sample, threshold, timer_on)
            global delta_off
            if(timer_off == delta_off): event_end = True

        # event_end = True # testar
        elif(is_on and event_start): 
            event.append(sample)
            print("EVENT HAPPENING!!")

     
        size = len(event)*1024 
        global max_samples
        if(size >= max_samples or event_end):
            full_event = np.concatenate(event, axis=0)
            print("SIZE EVENT: ", full_event.shape)
            event_start = False
            event_end = False
            event = []
            timer_on = 0
            timer_off = 0

        last_ind += 1024
        next_ind += 1024
    #return full_event

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
    #print("Threshold: ", threshold)
    return threshold


def on(y, threshold, time_on):
    on = analyze_rms(y, threshold)
    if on : time_on += 1
    return time_on

def off(y, threshold, time_off):
    off = not analyze_rms(y, threshold)
    if off : time_off += 1
    return time_off



if __name__ == "__main__":
    #print("Listening...")
    event_detection_file_test()
    #print("End")

    #audioname = "SonsTeste_SNR60 Mixdown_Cidade1.wav"      # testar real audio 
    #y, sr = librosa.load(audioname, mono=True)
    #print(y.shape)
