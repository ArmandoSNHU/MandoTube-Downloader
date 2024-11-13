
from pytube import YouTube

def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        messagebox.showinfo("Success", "Download completed!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up tkinter window
root = tk.Tk()
root.title("Mando Tube Downloader")

# URL input
tk.Label(root, text="YouTube URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

root.mainloop()

