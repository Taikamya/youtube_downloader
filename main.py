from pytube import YouTube
from sys import argv
from settings import URL

# getting the YT link from input
# url = input("What's the YT URL? \n")

# hard-coded YT link -- ONLY USE FOR TESTING --
# url = URL

# YT link from first argument in the CLI
url = argv[1]

yt_obj = YouTube(url)


if __name__=="__main__":
    print(f"Title: {yt_obj.title}\nViews: {yt_obj.views}")
