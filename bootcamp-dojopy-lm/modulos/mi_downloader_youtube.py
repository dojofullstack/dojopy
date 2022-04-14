from pytube import YouTube


print('descargando....')
video_url = 'https://www.youtube.com/watch?v=ZS1XDR7JASA'
# YouTube(video_url).streams.first().download()
yt = YouTube(video_url)
yt.streams.filter(progressive=True, file_extension='mp4') \
            .order_by('resolution'). \
            desc().first().download()
print('se descargo correctamente!')