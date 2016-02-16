from __future__ import unicode_literals
import youtube_dl

class Downloader:
    def __init__(self,url):
        self.url = url
        self.file_name = ""

    def my_hook(self,d):
        self.file_name = d['filename']
 
    def download(self):
        ydl_opts = {
                        "restrictfilenames":True,
                        "write_subtitles":True,
                        "writeinfojson":True,
                        "progress_hooks":[self.my_hook]
                      }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            downloaded = ydl.download([self.url])
        return self.file_name

downloader = Downloader("https://www.youtube.com/watch?v=LL9YgFEHW5U")
filename = downloader.download()
print(filename)
