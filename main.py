from pytube import YouTube
from tkinter import *
import os




janela = Tk()
janela.title('YoutubeDownloader')
janela.geometry('350x500')


video_link = StringVar()

def mp4_download():
    myVideoStream = YouTube(video_link.get()).streams
    mp4Streams = myVideoStream.filter(file_extension = "mp4")
    mp4Streams.first().download('downloads/')



def mp3_download():
    yt = YouTube(str(video_link.get()))
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path='downloads')

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    



logo = PhotoImage(file='assets\images\logo.png')
logo_label = Label(janela, image=logo)
logo_label.grid(column=0, row=0, pady=20)

texto_link = Label(janela, text='Link do Vídeo', font='64')
texto_link.grid(column=0, row=2)

entrada = Entry(janela, textvariable=video_link)
entrada.grid(column=0, row=3, pady=10)

mp4_img = PhotoImage(file='assets\images\mp4.png')
mp4_botao = Button(janela, image=mp4_img, command=mp4_download)
mp4_botao.grid(column=0, row=6)

mp3_img = PhotoImage(file='assets\images\mp3.png')
mp3_botao = Button(janela, image=mp3_img, command=mp3_download)
mp3_botao.grid(column=0, row=7)

playlist_img = PhotoImage(file='assets\images\playlist.png')
playlist_botao = Button(janela, image=playlist_img)
playlist_botao.grid(column=0, row=8)


janela.mainloop()