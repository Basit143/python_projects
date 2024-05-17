# main.py
from pytube import YouTube

def download_video(url, resolution='720p'):
    try:
        yt = YouTube(url)
        # Filter streams by progressive (video and audio in a single file)
        # Order them by resolution
        streams = yt.streams.filter(progressive=True).order_by('resolution')
        # Find the first stream with the specified resolution
        stream = streams.filter(res=resolution).first()
        if stream:
            # Download the stream
            stream.download()
            print("Download completed successfully!")
        else:
            print("No stream with the specified resolution found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)




