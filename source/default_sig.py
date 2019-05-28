import wave
from pydub import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_name="../voice_trim/fast1.wav"
#音声ファイルの読み込み
sound = AudioSegment.from_file(file_name,"wav")

#listに変換する
samples=sound.get_array_of_samples()

#実際に用いる部分の信号のみ表示
#plt.xlim([130000,200000])

#凡例の追加を行う
plt.plot(samples)
plt.show()