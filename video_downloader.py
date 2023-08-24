from pytube import YouTube

link="paste_the_youtube_video_link_here_to_download"

youtube_1=YouTube(link)

videos=youtube_1.streams.all()
vid=list(enumerate(videos))
for i in vid:
    print(i)

print()
strm=int(input("enter :"))
videos[strm].download()
print('succesfully')
