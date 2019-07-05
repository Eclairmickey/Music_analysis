import wave
import os
from pydub import *
import numpy as np
import matplotlib.pyplot as plt
import math

##サンプリング開始位置
start=0
#サンプル数
N=512

#パスの指定
path="../trim_voice/"
direct=os.listdir(path)

i=0
for name in direct:
    if os.path.exists(path+name) :
        #path結合して音源の読み込み
        file_name=path+name
        sound=AudioSegment.from_file(file_name,"wav")

        # 音声データを配列で抽出し,numpyに変換 
        sound_ar = sound.get_array_of_samples()
        soundnp=np.array(sound_ar)

        #numpyにステレオ音源の片側の音源を抽出しておく
        sample =soundnp[::sound.channels]


        #窓関数(hammingwindowをかける)
        HammingWindow=np.hamming(N)
        x=HammingWindow*sample[start:N+start]

        #FFT
        spec=np.fft.fft(x)

        #パワースペクトル
        fft_signal_power=abs(spec)**2

        #分析の長さで割る
        fft_signal_power=fft_signal_power/N
        
        num=i%3
        
        plt.subplot(1,3,num+1)
        plt.xlabel("frequency[Hz]")
        plt.ylabel("Power[msec^2/Hz]")
        if i<3:
                title="Speaker"+str(i+1)
                plt.title(title)
                speed="fast"
        else:
                speed="slow"
       
        #信号をグラフにプロットする
        plt.plot(fft_signal_power,label=speed)
        plt.legend(loc=(0.6,0.8))
        i+=1

plt.show()
