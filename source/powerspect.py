import wave
import os
from pydub import *
import numpy as np
import matplotlib.pyplot as plt
import math
start=0
N=512

#パスの指定
path="../trim_voice/"
direct=os.listdir(path)

i=0
for x in direct:
    if os.path.exists(path+x):
        #path結合して音源の読み込み
        file_name=path+x
        sound=AudioSegment.from_file(file_name,"wav")
        print(sound.frame_rate)
        # 音声データをリストで抽出 
        sound_ar = sound.get_array_of_samples()

        #numpyにステレオ音源の片側の音源を抽出しておく
        sample =sound_ar[::sound.channels]

        #正規化
        x=np.frombuffer(sample,dtype="int16")/32768.0

        #窓関数(hammingwindowをかける)
        HammingWindow=np.hamming(N)
        x=HammingWindow*sample[start:N+start]

        #FFT
        spec=np.fft.fft(x)

        #パワースペクトル
        fft_signal_power=np.sqrt(abs(spec))

        #分析の長さで割る
        fft_signal_power=fft_signal_power/N

        #デシベル換算
        fft_signal_power=10*np.log10(fft_signal_power)

        
        num=i%3
        plt.subplot(1,3,num+1)
        print(i,',',num)
        #信号をグラフにプロットする
        plt.plot(fft_signal_power)
        i+=1

plt.show()
