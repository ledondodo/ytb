# importing packages
from pytube import YouTube
import os

path = "/Users/arthurchansel/Downloads"

# === FUNCTIONS ===

def prRed(skk): print("\033[0;91m{}\033[00m" .format(skk))

def download_one(mylink, path, myext):
    yt = YouTube(mylink) # url
    video = yt.streams.filter(only_audio=True).first() # extract audio
    out_file = video.download(output_path=path) # download the file
    base, ext = os.path.splitext(out_file)
    if myext == 'wav':
        os.rename(out_file, base + '.wav')
    elif myext == 'mp3':
        os.rename(out_file, base + '.mp3')
    else:
        print('Wrong extension: ' + myext)
        return False
    prRed(yt.title + ' has been successfully downloaded (' + myext + ').\n')
    return True

# === MAIN ===

print('\n\t--- YouTube Download ---')
myvideo = input('Video url: ')
ext = input('Extension (wav or mp3): ')
download_one(myvideo, path, ext)