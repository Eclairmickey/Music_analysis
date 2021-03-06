import wave
import os
from pydub import *
import numpy as np
import matplotlib.pyplot as plt

start=0
N=512

#パスの指定
path="../voice_trim/"
direct=os.listdir(path)

i=0
for x in direct:
    if os.path.exists(path+x):
        #path結合して音源の読み込み
        
        file_name=path+x
        sound=AudioSegment.from_file(file_name,"wav")

        #音声データをリストで抽出 
        sound_ar = sound.get_array_of_samples()

        #numpyにステレオ音源の片側の音源を抽出しておく
        sample =sound_ar[::sound.channels]

        #窓関数(hammingwindowをかける)
        HammingWindow=np.hamming(N)
        x=HammingWindow*sample[start:N+start]

        #フーリエ変換を行う
        spec=np.fft.fft(x)

        num=i%3
        plt.subplot(1,3,num+1)
        print(i,',',num)
        #信号をグラフにプロットする
        plt.plot(spec)
        i+=1

plt.show()
