from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil
import tkinter.messagebox as tmsg

def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    tmsg.showinfo("Downloading...","Downloading in Process")

    mp4_vdo = YouTube(get_link).streams.first().download()
    vid_clip = VideoFileClip(mp4_vdo)
    vid_clip.close()

    shutil.move(mp4_vdo, user_path)
    tmsg.showinfo("Downloading completed","Downloaded Successfully!")


root = Tk()
root.geometry("744x545")
root.title("Youtube Downloader")
root.wm_iconbitmap("C:\SIMAR\MyProjects\Youtube Downloader/yt_icon.ico")

# LOGO IMAGE
logo_img = PhotoImage(file="C:\SIMAR\MyProjects\Youtube Downloader/yt.png")
canvas = Canvas(root, width=500, height=150)
canvas.pack()
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250,80,image= logo_img)

# LINK FIELD
link_field = Entry(root, width=40 , font = "Arial 15")
Label(root, text= "Enter download link: ", font ="Arial 15").pack(pady=5)
link_field.pack(pady=10)

# SELECT PATH
path_label = Label(root, text= "Select path for download",font="Arial 15")
path_label.pack(pady=10)
path_btn = Button(root,text="Select Path",bg="red",fg="white",font="Arial 15",padx=22,pady=5,command=select_path)
path_btn.pack()

# DOWNLOAD BUTTON
download_btn = Button(root,text="Download File",bg="green",fg="white",font="Arial 15",padx=22,pady=5,command=download_file)
download_btn.pack(pady=10)

root.mainloop()