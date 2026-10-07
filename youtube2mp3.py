#!/usr/bin/env python3

from pytubefix import YouTube
from pytubefix import Playlist
import sys
import concurrent.futures

def download_audio(url):
	print("downloading audio from " + url)
	# url input from user
	yt = YouTube(str(url))

	# extract only audio
	# try mp4 first, then mp3, and finally whatever is available
	out_file = None
	s = yt.streams.filter(type="audio", progressive=False, mime_type="audio/mp4")
	if s.first():
		out_file = s.first().download()
	else:
		s = yt.streams.filter(type="audio", progressive=False, mime_type="audio/mp3")
		if s.first():
			out_file = s.first().download()
		else:
			s = yt.streams.filter(only_audio=True).first()
			if s:
				out_file = s.download()

	if out_file:
		print(f"'{yt.title}' has been downloaded to '{out_file}'")
	else:
		print(f"unable to download {yt.title}")

def main(args):
	failed = False
	with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
		futures = {}
		for arg in args:
			if "playlist?" in arg:
				playlist = Playlist(str(arg))
				urls = playlist.video_urls
			else:
				urls = [arg]
			for url in urls:
				futures[pool.submit(download_audio, url)] = url
		for future in concurrent.futures.as_completed(futures):
			try:
				future.result()
			except Exception as exc:
				failed = True
				print(f"unable to download {futures[future]}: {exc}", file=sys.stderr)
	return 1 if failed else 0


if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
