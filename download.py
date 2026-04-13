import yt_dlp


def download_video(url):
    ydl_opts = {
        'outtmpl': 'video.mp4',
        'format': 'best[filesize<50M]'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
