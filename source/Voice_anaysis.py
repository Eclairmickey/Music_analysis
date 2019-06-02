import wave
import os
from pydub import *
import scipy.fftpack
import numpy as np
import matplotlib.pyplot as plt

path="../sample_voice/"
# 音声ファイルの読み込み
print(os.listdir(path))
direct=os.listdir(path)
#sound = AudioSegment.from_file(file_name,"wav")

for x in direct:
    if os.path.isdir(path+x):
        file_name=path+x
        sound=AudioSegment.from_file(file_name,"wav")

        # 音声データをリストで抽出
        list_sound = sound.get_array_of_samples()

        #numpyにステレオ音源の片側の音源を抽出しておく
        sample=np.array(sound.get_array_of_samples())

        #元々の入力信号を左側に表示
        plt.xlabel("Time")
        plt.ylabel("Signal")
        plt.plot(sample)

        #正規化
        x=np.frombuffer(sample,dtype="int16")/32768.0

        #点を取る位置、数を設定
        start=0
        N=256

        #窓関数(hammingwindowをかける)
        HammingWindow=np.hamming(N)
        x=HammingWindow*sample[start:N+start]

        spec=np.fft.fft(x)
        Amp=np.abs(spec)

        #信号をグラフにプロットする(右側に表示)
        #plt.subplot(122)
        plt.xlabel("Frequency")
        plt.ylabel("Amplitude")
        plt.plot(Amp)
        plt.show()
