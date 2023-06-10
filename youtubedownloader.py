import tkinter as tk
import customtkinter as ctk
from pytube import YouTube

root = ctk.CTk()

def startdownload():
    try:
        ytlink = entry_label.get()
        ytObject = YouTube(ytlink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        finished_label.configure(text = "Download error")
    finished_label.configure(text= "Downloaded!")

ctk.set_default_color_theme('blue')
ctk.set_appearance_mode('dark')

root.geometry("720x480")
root.title("Mai's youtube downloader")

title_label = ctk.CTkLabel(root, text="Enter youtube link here:", font = ctk.CTkFont( size = 40, weight="bold" ))
title_label.pack( padx = 20, pady = 20)


getlink = tk.StringVar()
entry_label = ctk.CTkEntry(root, width= 500, textvariable= getlink )
entry_label.pack(padx=10, pady= 10)

button_label = ctk.CTkButton(root, text = "Download", width = 144, height = 60, command= startdownload)
button_label.pack(padx = 10, pady = 5)

finished_label = ctk.CTkEntry(root, text = " ")
finished_label.pack()

root.mainloop()