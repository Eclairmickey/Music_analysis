#from pydub import AudioSegment
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import wave

#パスの指定
path="../trim_voice/"
direct=os.listdir(path)

#サンプル数
N=512

i=0
for x in direct:
    if os.path.exists(path+x):
        #path結合して音源の読み込み
        file_name=path+x
        # WAVEファイルから波形データを取得
        wf = wave.open(file_name, "rb")
        data = wf.readframes(wf.getnframes())
        data = np.frombuffer(data, dtype="int16")
        length = float(wf.getnframes()) / wf.getframerate() #波形長さ（秒）


        #窓関数(hammingwindowをかける)
        hammingWindow=np.hamming(N)

        #スペクトグラムの出力
        plt.subplot(2,3,i+1)
        plt.title(x)
        pxx, freqs, bins, im = plt.specgram(data, NFFT=N, Fs=wf.getframerate(), noverlap=0, window=hammingWindow)
        plt.axis([0, length, 0, wf.getframerate() / 2])
        plt.xlabel("time [second]")
        plt.ylabel("frequency [Hz]")
        i+=1
       
plt.show()