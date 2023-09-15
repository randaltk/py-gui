import tkinter as tk
from pytube import YouTube

app = tk.Tk()
app.geometry("720x480")
app.title("Youtube Downloader")


download_button = tk.Button(app, text="Download")

status_label = tk.Label(app, text="")
status_label.pack()


app.mainloop()
