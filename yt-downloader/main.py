from pytube import YouTube
directory = './yt-downloader'

def downloadVideo(url):
  video = YouTube(url)
  print(f'🙂 Downloading...')
  video.streams.get_highest_resolution().download(directory)
  print(f'🥳 Video downloaded successfully: {video.title}')

videoUrl = str(input('⚡ Insert the link of the video you want to download: '))
downloadVideo(videoUrl)