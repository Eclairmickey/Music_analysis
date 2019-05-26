from __future__ import print_function
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

#音源読み込み(audio.load(ファイル名,offset,duration))
#offset部分からdurationで設定した秒数分切り出し
file_name="Sanple_tempo\bpm150.mp3"
music,fs=librosa.audio.load(file_name,"mp3")

#フーリエ変換
#S=np.abs(librosa.stft(y))

#BPM取り出し
tempo,beats=librosa.beat.beat_track(y=music,sr=fs)
#librosa.display.waveplot(music,fs)

plt.plot(beats)
plt.show()

print(tempo)
print(beats)
#画像出力
"""
plt.figure(figsize=(10,4))
librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), y_axis='log', x_axis='time')
plt.title('Power spectrogram')
plt.colorbar(format='%+2.0f dB')
 
plt.tight_layout()
plt.show()
"""