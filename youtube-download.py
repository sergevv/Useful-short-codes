# ---------- Download video from youtube ------------ #
# More info about pytube library: https://pytube.io/

from pytube import YouTube
link = 'https://www.youtube.com/watch?v=2PjZAeiU7uM'
yt = YouTube(link)
yt.streams.filter(mime_type="video/mp4",          # type
                  res='360p').first().download()  # resolution
