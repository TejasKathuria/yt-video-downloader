import tkinter
from tkinter import filedialog
import customtkinter
from pytube import YouTube


def downloadvid():
    try:
        ytlink = link.get()
        obj = YouTube(ytlink)
        vid = obj.streams.get_highest_resolution()
        vid.download()
    except:
        print("Error: The Link is invalid")
    print("The download has successfully been completed!")

customtkinter.set_appearance_mode("System")

app = customtkinter.CTk()
app.geometry("728x619")
app.title("YT Downloader By Tejas K")

#Main Elements
heading = customtkinter.CTkLabel(app, text="Paste your YouTube Link here")
heading.pack(padx=10, pady=10)

mainUrl = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=345, height=40, textvariable=mainUrl)
link.pack()

downloadbtn = customtkinter.CTkButton(app, text="Download Video", command=downloadvid)

app.mainloop()