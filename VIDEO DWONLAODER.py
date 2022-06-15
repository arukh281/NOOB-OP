from pytube import YouTube
yt = YouTube('https://youtu.be/uyEIihDoXR8')
yt = yt.streams.get_highest_resolution()
yt.download()
