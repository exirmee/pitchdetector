import parselmouth
import numpy as np 
import pyaudio
import queue
import music21
import datetime
import aubio
# Open stream.
# PyAudio object.
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1, rate=44100, input=True,
                input_device_index=0, frames_per_buffer=512)

q = queue.Queue()  

current_pitch = music21.pitch.Pitch()
def get_current_note():
    while True:
        data = stream.read(2048, exception_on_overflow=False)
        samples = np.fromstring(data,dtype=aubio.float_type)
        sndMic = parselmouth.Sound(samples)
        pitch = sndMic.to_pitch()
        pitch_values = pitch.selected_array['frequency']
        pitch_values[pitch_values==0] = np.nan
        
        current='Nan'
        if pitch_values[0]>0:
            current_pitch.frequency = pitch_values[0]
            current=current_pitch.nameWithOctave
            print(pitch_values,'----',current)
        q.put({'Note': current, 'Cents': current_pitch.microtone.cents,'hz':current_pitch.frequency})
    

if __name__ == '__main__':
    get_current_note()
    

