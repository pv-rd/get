import numpy as np
import time 
def get_sin_wave_amplitude(f, t):
    return (np.sin(2 * np.pi * f * t) + 1)/2

def wait_for_sampling_period(f):
    time.sleep(1/f)