import pytube
from pytube import YouTube
import tkinter as tk
from  tkinter import messagebox, filedialog

def vdo_info() :
    url = entry_url.get()
    try :
        video= pytube.YouTube(url)
        views = video.views
        title = video.title
        label_title.config(text ="Title :" + title)
        label_views.config(text="Views :"+ str(views))
        return video
    except pytube.exceptions.PytubeError as e:
        messagebox.showerror("Error" ,str(e))

def choose_dir() :
    download_dir = filedialog.askdirectory()
    entry_dir.delete(0,tk.END)
    entry_dir.insert(0,download_dir)

def vdo_download() :
    video = vdo_info()
    if video :
        try:
            stream = video.streams.get_highest_resolution()
            download_dir = entry_dir.get()
            stream.download(download_dir)
            messagebox.showinfo("Success","video downloaded successfully")
        except pytube.exceptions.PytubeError as e:
            messagebox.showerror("Error",str(e))

def audio_download() :
    video = vdo_info()
    if video:
        try:
            stream = video.streams.get_audio_only()
            download_dir = entry_dir.get()
            stream.download(download_dir)
            messagebox.showinfo("Success", "Audio downlaoded successfully!")
        except pytube.exceptions.PytubeError as e:
            messagebox.showerror("Error",str(e))

window = tk.Tk()
window.title("YouTube Video & Audio downloader")

label_url = tk.Label(window, text="Enter the video URl : ")
label_url.pack()
entry_url = tk.Entry(window, width=50)
entry_url.pack()

label_directory = tk.Label(window,text = "Choose Download Directory")
label_directory.pack()
entry_dir=tk.Entry(window,width=50)
entry_dir.pack()

button_dir = tk.Button(window,text="Select Directory",command = choose_dir )
button_dir.pack()

button_info = tk.Button(window,text= "Get Video Info.", command=vdo_info)
button_info.pack()

button_vdo = tk.Button(window,text="Download Video",command = vdo_download)
button_vdo.pack()

button_audio = tk.Button(window,text="Download Audio",command = audio_download)
button_audio.pack()

label_title = tk.Label(window,text="Title : ")
label_title.pack()

label_views = tk.Label(window,text="Views : ")
label_views.pack()

window.mainloop()

