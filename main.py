import tkinter as tk
from pytube import YouTube


def download_video():
    video_url = url_entry.get()
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    status_label.config(text="Download complete")


app = tk.Tk()
app.geometry("720x480")
app.title("Youtube Downloader")


url_label = tk.Label(app, text="Enter YouTube URL:")
url_label.pack()
url_entry = tk.Entry(app, width=40)
url_entry.pack()


download_button = tk.Button(app, text="Download", command=download_video)
download_button.pack()

status_label = tk.Label(app, text="")
status_label.pack()


app.mainloop()
