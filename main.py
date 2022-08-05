from pytube import YouTube
from sys import argv
from settings import URL

# getting the YT link from input
# url = input("What's the YT URL? \n")

# hard-coded YT link -- ONLY USE FOR TESTING --
url = URL

# YT link from first argument in the CLI
# url = argv[1]

yt_obj = YouTube(url)

downloader_obj = yt_obj.streams.get_highest_resolution()

def download(link) -> None:
    if downloader_obj != None:
        print("Video found. Begin downloading...")
    else:
        print("Video not found. Invalid link.")
    link.download("./downloads/")


if __name__=="__main__":
    # Testing purposes
    print(f"Title: {yt_obj.title}\nViews: {yt_obj.views}")
    # ---------------------------- // ----------------------------
    # Download if all ok
    download(downloader_obj)
