from pytube import YouTube
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


url = input("Enter Link Here: ")
start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))
print("Processing, please wait......")
yt = YouTube(url)
out_put = yt.streams.get_highest_resolution().download()
os.rename(out_put, 'test.mp4')
ffmpeg_extract_subclip('test.mp4', (start), (end), targetname="test1.mp4")
os.remove("test.mp4")




