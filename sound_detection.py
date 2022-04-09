### sound detection

import librosa
import numpy as np

def sound_features():
    sound_list =['audioHalf1.wav', 'audioHalf2.wav']
    features = []
    for sound in sound_list:
        sound_features = []
        y, sr = librosa.load(sound, mono=True, duration=5)
        rms = librosa.feature.rms(y=y)
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        sound_features.append(np.mean(chroma_stft))
        sound_features.append(np.mean(rms))
        sound_features.append(np.mean(spec_cent))
        sound_features.append(np.mean(spec_bw))
        sound_features.append(np.mean(rolloff))
        sound_features.append(np.mean(zcr))
        for e in mfcc:
            sound_features.append(np.mean(e))
        features.append(sound_features)
    features = np.array(features)
    return features
