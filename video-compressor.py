import os, subprocess

count = 0
videosLocation = '/mnt/e/Edições/ToCompress'
videosNames = os.listdir(videosLocation)

os.chdir(videosLocation)

for videoName in videosNames:
  subprocess.call([
    'ffmpeg', '-i', videoName, '-vcodec', 'h264', '-acodec', 'mp2', '-b:v',
    '5M', '-maxrate', '7M', '-bufsize', '3M', f'Video{count}.mp4'
  ])
  count += 1
