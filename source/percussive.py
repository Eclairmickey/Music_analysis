import matplotlib
matplotlib.use("tkagg")

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

#音源読み込み(audio.load(ファイル名,offset,duration))
#offset部分からdurationで設定した秒数分切り出し
file_name="Sample_Song/For_ultra.mp3"
music,fs=librosa.audio.load(file_name)


#短時間フーリエ変換
D=librosa.stft(music)

D_harmonic,D_percussive=librosa.decompose.hpss(D)

#グラフ描画
#周波数成分が一番大きいものを取る
rp=np.max(np.abs(D))
plt.figure(figsize=(12,8))
#周波数ごとの振幅スペクトログラムをプロット
librosa.display.specshow(librosa.amplitude_to_db(np.abs(D_percussive),ref=rp),y_axis='log',x_axis='time')
plt.colorbar()
plt.show()
print(D_percussive)
