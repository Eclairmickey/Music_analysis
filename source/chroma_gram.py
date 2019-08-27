import matplotlib
matplotlib.use("tkagg")

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

#sampling_rate(サンプリング周波数)
sr=44100

#音源読み込み(audio.load(ファイル名,offset,duration))
#offset部分からdurationで設定した秒数分切り出し
file_name="Sample_Song/AtlanticoBlue.mp3"
music,fs=librosa.audio.load(file_name,sr=sr)


#打楽器成分とメロディ成分に分ける
D_harmonic,D_percussive=librosa.decompose.hpss(D)

#クロマグラムを構成
"""
内部の動作概要
1.メロディ成分を周波数ごとに切り取る
2.それぞれの周波数の塊ごとに細分化をまた行う
3.それぞれの周波数の1オクターヴ単位で同じ音を固める
つまり音を1つのオクターヴに押し込むことを行っている
"""
C=librosa.feature.chroma_cens(y=D_harmonic,sr=sr)

#プロット部分




