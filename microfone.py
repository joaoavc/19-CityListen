### microfone

import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment


def listen_audio():
    i=0
    listen = True
    process = True
    while(listen):
        while(process):
            i += 1 
            fs = 44100  # Sample rate
            seconds = 10  # Duration of recording
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()  # Wait until recording is finished
            write('audioRecord.wav', fs, myrecording)  # Save as WAV file
            process = False
        process = True
        if(i > 1):
            listen = False


def split_sound():
    t1 = 0 * 1000 #Works in milliseconds
    t2 = 5 * 1000
    t3 = 10 *1000
    audio = AudioSegment.from_wav('audioRecord.wav')
    audioHalf1 = audio[t1:t2]
    audioHalf2 = audio[t2:t3]
    audioHalf1.export('audioHalf1.wav', format="wav") #Exports to a wav file in the current path.
    audioHalf2.export('audioHalf2.wav', format="wav") #Exports to a wav file in the current path.


if __name__ == "__main__":
    print ("Listening...")
    listen_audio()
    split_sound()
    print("End")
