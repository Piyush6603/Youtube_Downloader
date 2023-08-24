from pytube import Playlist

py=Playlist("paste_the_youtube_playlist_link_here_to_download")

print(f'downloading:{py.title}')

for video in py.videos:
    video.streams.first().download()
