###---------- Download video from youtube ------------###
# More info about pytube library: https://pytube.io/

from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=2PjZAeiU7uM')    # youtibe direct link
yt.streams.filter(mime_type="video/mp4", res='144p').first().download()    # type and resolution
