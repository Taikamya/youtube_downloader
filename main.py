from pytube import YouTube
from sys import argv
from settings import URL

# soft-coded link
# url = input("What's the YT URL? \n")

# hard-coded link -- ONLY USE FOR TESTING --
url = URL

# link from first argument in the CLI
# url = argv[1]

def secure_url() -> str:
    '''Secure URL check function'''
    if url[0:5] == "http:":
        s_url = url.replace("http", "https")
    else:
        s_url = url
    return s_url

def download(link) -> None:
    '''Download function'''
    if downloader_obj != None:
        print("Video found. Begin downloading...")
    else:
        print("Video not found. Invalid link.")
    link.download("./downloads/")

# YT link
yt_obj = YouTube(secure_url())
# Highest resolution available
downloader_obj = yt_obj.streams.get_highest_resolution()


if __name__=="__main__":
    # Link info
    print(f"Title: {yt_obj.title}\nViews: {yt_obj.views}")
    # ---------------------------- // ----------------------------
    # Download if all ok
    download(downloader_obj)
