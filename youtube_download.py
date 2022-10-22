from pytube import YouTube

YouTube('https://youtu.be/HJv4L3Adnq8').streams.first().download()
yt = YouTube('https://youtu.be/HJv4L3Adnq8')
yt.streams # показывает какое видео ты можешь скачать 
# (mp4(720) + audio или только mp4(1080) без звука). 
# Сейчас стоит фильтр по mp4.
# print(yt.streams.filter(file_extension='mp4')) 
# stream = yt.streams.get_by_itag(22) #выбираем по тегу, в каком формате будем скачивать.
# stream.download() #загружаем видео.

