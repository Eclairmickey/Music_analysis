import wave
from pydub import *
import scipy.fftpack
import numpy as np
import matplotlib.pyplot as plt
# 音声ファイルの読み込み
file_name="../sample_voice/slow1.wav"
sound = AudioSegment.from_file(file_name,"wav")

# 音声データをリストで抽出
list_sound = sound.get_array_of_samples()

#numpyにステレオ音源の片側の音源を抽出しておく
sample=np.array(sound.get_array_of_samples())
#正規化
x=np.frombuffer(sample,dtype="int16")/32768.0

#点を取る位置、数を設定
start=0
N=256
#窓関数(hammingwindowをかける)
HammingWindow=np.hamming(N)
x=HammingWindow*sample[start:N+start]

spec=np.fft.fft(x)

#信号をグラフにプロットする
plt.plot(spec)
plt.show()
