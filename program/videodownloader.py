
from pytube import YouTube

video_link = str(input('Link do vídeo: '))

myVideoStream = YouTube(video_link).streams

webmStreams = myVideoStream.filter(file_extension = "mp4")

webmStreams.first().download('downloads/')

print('Baixado')