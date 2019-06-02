import wave
from pydub import *
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path="../sample_voice/"
# 音声ファイルの読み込み
print(os.listdir(path))
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
        sample=np.array(sound.get_array_of_samples())

        #実際に用いる部分の信号のみ表示
        #plt.xlim([130000,200000])

        num=i%3
        plt.subplot(1,3,num+1)
        print(i,',',num)
        #凡例の追加を行う
        plt.plot(sample)
        i+=1

plt.show()

        
