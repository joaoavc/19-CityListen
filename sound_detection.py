### sound detection

import librosa
import numpy as np
from microfone       import *



def sound_features(sound_record):

    sound_features = []
    y = sound_record.ravel()
    sr = 44100
    S = np.abs(librosa.stft(y))
    
    rms_avg_val = np.mean(librosa.feature.rms(y=y))
    sound_features.append(rms_avg_val)
    rms_std_val = np.std(librosa.feature.rms(y=y))
    sound_features.append(rms_std_val)
    spec_cent_avg_val = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
    sound_features.append(spec_cent_avg_val)
    spec_cent_std_val = np.std(librosa.feature.spectral_centroid(y=y, sr=sr))
    sound_features.append(spec_cent_std_val)
    spec_bw_avg_val = np.mean(librosa.feature.spectral_bandwidth(y=y, sr=sr))
    sound_features.append(spec_bw_avg_val)
    spec_bw_std_val = np.std(librosa.feature.spectral_bandwidth(y=y, sr=sr))
    sound_features.append(spec_bw_std_val)
    rolloff_avg_val = np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr))
    sound_features.append(rolloff_avg_val)
    rolloff_std_val = np.std(librosa.feature.spectral_rolloff(y=y, sr=sr))
    sound_features.append(rolloff_std_val)
    zcr_avg_val =  np.mean(librosa.feature.zero_crossing_rate(y))
    sound_features.append(zcr_avg_val)
    zcr_std_val =  np.std(librosa.feature.zero_crossing_rate(y))
    sound_features.append(zcr_std_val)
    flatness_avg_val = np.mean(librosa.feature.spectral_flatness(y=y))
    sound_features.append(flatness_avg_val)
    flatness_std_val = np.std(librosa.feature.spectral_flatness(y=y))
    sound_features.append(flatness_std_val)

    mfcc_vals = librosa.feature.mfcc(y=y, sr=sr)
    contrast_vals = librosa.feature.spectral_contrast(S=S, sr=sr)  
    
    for mfcc_val in mfcc_vals:
        sound_features.append(np.mean(mfcc_val))
        sound_features.append(np.std(mfcc_val))
        
    for contrast_val in contrast_vals:
        sound_features.append(np.mean(contrast_val))
        sound_features.append(np.std(contrast_val))
    
    features = []
    features.append(sound_features)
    features = np.array(features)
    return features


def analyze_rms(sound_record, threshold):
    y = sound_record.ravel()
    rms = librosa.feature.rms(y=y)
    bigger_than = rms[rms>=10]. astype('float64')
    return rms.shape[0] > 0



def analyze_spectrual_flux(sound_record, threshold):
    sample_rate = 44100
    y = sound_record.ravel()
    onset_env = librosa.onset.onset_strength(y=data, sr=sample_rate)
    return any(i >= threshold for i in onset_env)


    

    
