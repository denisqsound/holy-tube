from pytube import YouTube

# url_for_download = input("Вставь url для скачивания: ")
# print(url_for_download)
url_for_download = ""

my_video = YouTube(url_for_download)
my_video = my_video.streams.get_highest_resolution()
my_video.download()
