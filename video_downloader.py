from pytube import YouTube

# Replace 'video_url' with the URL of the YouTube video you want to download
video_url = 'https://www.youtube.com/watch?v=PArS4YeAq8w'

try:
    # Create a YouTube object
    yt = YouTube(video_url)
    
    # Get the highest resolution stream available (streams are sorted by resolution)
    stream = yt.streams.get_highest_resolution()
    
    # Specify the directory where you want to save the video
    save_path = 'paste_the_path_of_your_directory_here'
    
    # Download the video to the specified path
    stream.download(output_path=save_path)
    
    print('Download completed!')
except Exception as e:
    print('An error occurred:', str(e))
