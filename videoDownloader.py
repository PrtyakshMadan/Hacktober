from pytube import YouTube
import os

video_url = "https://youtu.be/T1fkvT1uPj8?si=kPkzbC0b0582X1fU"
save_path = "C:/Users/prtya/ml"
def youtube_downloader(video_url,save_path):
    video = YouTube(video_url)
    audio_stream = video.streams.first()

    if not os.path.exists(save_path): 
        os.makedirs(save_path)

    audio_file_path = audio_stream.download(output_path=save_path)

    return audio_file_path

download_path = youtube_downloader(video_url,save_path)


