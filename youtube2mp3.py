#!/usr/bin/env python3

from pytubefix import YouTube
from pytubefix import Playlist
import sys
import concurrent.futures
import argparse

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
		raise RuntimeError(f"no audio downloaded for '{yt.title}' (no available audio stream or output file)")

def main(args=None):
	parser = argparse.ArgumentParser(
		description="Download audio from YouTube videos or playlists to the current directory.",
		epilog='Keeps the original audio format; does not convert to mp3. '
		       'Quote URLs containing shell characters such as &. '
		       'Example: %(prog)s "https://www.youtube.com/watch?v=VIDEO_ID"',
	)
	parser.add_argument("urls", metavar="URL", nargs="+", help="YouTube video or playlist URL")
	options = parser.parse_args(args)
	failed = False
	with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
		futures = {}
		for arg in options.urls:
			if "playlist?" in arg:
				try:
					urls = list(Playlist(str(arg)).video_urls)
					if not urls:
						raise RuntimeError("playlist contains no available videos")
				except Exception as exc:
					failed = True
					print(f"unable to load playlist {arg}: {exc}", file=sys.stderr)
					continue
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
