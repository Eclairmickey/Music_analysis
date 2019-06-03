import wave
import os
from pydub import *
import numpy as np
import matplotlib.pyplot as plt

#点を取る位置、数を設定
start=0
N=256

#パスの指定
path="../sample_voice/"
direct=os.listdir(path)


i=0
for x in direct:
    if os.path.exists(path+x):
        #path結合して音源の読み込み
        file_name=path+x
        sound=AudioSegment.from_file(file_name,"wav")


        # 音声データをリストで抽出 
        list_sound = sound.get_array_of_samples()

        #numpyにステレオ音源の片側の音源を抽出しておく
        sample=np.array(list_sound)

        #正規化
        x=np.frombuffer(sample,dtype="int16")/32768.0

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
