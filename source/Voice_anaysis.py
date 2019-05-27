import wave
from pydub import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_name="../sample_voice/fast1.wav"
# 音声ファイルの読み込み
sound = AudioSegment.from_file(file_name,"wav")


#チャンネル数(1:mono,2:stereo)
sound.channels

# 音声データをリストで抽出
list_sound = sound.get_array_of_samples()

#numpyにステレオ音源の片側の音源を抽出しておく
samples=np.array(sound.get_array_of_samples())
sample=samples[::sound.channels]

spec=np.fft.fft(sample)

#信号をグラフにプロットする
plt.plot(spec)
plt.show()
