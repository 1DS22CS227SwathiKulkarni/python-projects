from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil

def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    print('Downloading...')
    mp4= YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)
    #code for mp3
    audio_file = video_clip.audio
    audio_file.write_audiofile('audio.mp3')
    audio_file.close()
    shutil.move('audio.mp3', file_path)
    #code for mp3
    video_clip.close()
    shutil.move(mp4, file_path)
    print('Download Complete!')

def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

root = Tk()

root.title('Video Downloader')
canvas = Canvas(root, width=400, height=300)
canvas.pack()

#app_label 
app_label = Label(root, text="Video Downloader", fg='blue', font=('Arial', 20))
canvas.create_window(200, 20, window=app_label)

#entry to accept video url
url_label = Label(root, text='Enter Video URL')
canvas.create_window(200,80, window=url_label)
url_entry = Entry(root)
canvas.create_window(200,100, window=url_entry)

#path to download video
path_label = Label(root, text='Select path for download')
canvas.create_window(200,150, window=path_label)
path_button = Button(root, text='Select', command=get_path)
canvas.create_window(200,170, window=path_button)

#download button
download_button = Button(root, text='Download', command=download)
canvas.create_window(200,250, window=download_button)

root.mainloop()