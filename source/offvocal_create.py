import scipy
import sys
from pydub import AudioSegment
import wave


def main():
  #ファイルパスを格納する変数
  filepath=""
  
  #ファイルパスからロードする
  wf=wave.open(file_name,'r')
  
  channels=fs.getchannels()
  fs=wf.getframerate()
  nframes=wf.getnframes()
  framerate=wf.getframerete()
  ss=wf.getsampwidth()
  
  print("channels:{},framerate:{},totalframes:{}".format(fs,framerate,nframes)
  
  #バイナリに変換
  data=wf.readframes(getnframes)
  
  #Numpy配列に変換
  data=np.frombuffer(data,dtype="int%d" % (8 *ss))
  
  
  
  
  
 #https://github.com/gifunogi/DigitalSignalProcessing
 
  
