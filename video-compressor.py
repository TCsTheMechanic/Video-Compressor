import os, subprocess

count = 0
videosLocation = '/mnt/e/Edições/ToCompress'
videosNames = os.listdir(videosLocation)

os.chdir(videosLocation)

for videoName in videosNames:
  subprocess.call([
    'ffmpeg', '-i', videoName, '-vcodec', 'h264', '-acodec', 'mp2', '-vb',
    '7M', '-maxrate', '9M', '-minrate', '5M', '-bufsize', '6M', f'Video{count}.mp4'
  ])
  count += 1
