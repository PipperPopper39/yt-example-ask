import yt_dlp


def youtube_dl_handler(url):
    print("Youtube DL Handler")


    def my_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')

    class MyLogger(object):
        def debug(self, msg):
            print(msg)

        def warning(self, msg):
            print(msg)

        def error(self, msg):
            print(msg)

    ydl_opts = {
        'format:': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
        'outtmpl': "%(title)s.%(ext)s",
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'cachedir': False,
        "postprocessors": [{
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mp4",
        }],
        "verbose": True,
        "print-traffic": True,
        
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Calling Handler")
            ydl.download([url])
        print("Youtube DL Handler Done")
    except Exception as e:
        raise Exception(e)

youtube_dl_handler("https://www.youtube.com/watch?v=U1a73gdNs0M")