# importing packages
from pytube import YouTube
import os

path = "/Users/arthurchansel/Downloads"

# === FUNCTIONS ===

def prRed(skk): print("\033[0;91m{}\033[00m" .format(skk))

def download_one(mylink, path):
    yt = YouTube(mylink) # url
    video = yt.streams.filter(only_audio=True).first() # extract audio
    out_file = video.download(output_path=path) # download the file
    base, ext = os.path.splitext(out_file)
    os.rename(out_file, base + ".wav")
    prRed(yt.title + " has been successfully downloaded (wav).\n")

# === MAIN ===

print('\n\t--- YouTube Download ---')
myvideo = input("Video url: ")
download_one(myvideo, path)