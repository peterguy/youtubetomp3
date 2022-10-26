#!/usr/bin/env python3

from pytube import YouTube
from pytube import Playlist
import os
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
			if s.first():
				out_file = s.first().download()

	if out_file:
		print(f"'{yt.title}' has been downloaded to '{out_file}'")
	else:
		print(f"unable to download {yt.title}")

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:	
	for arg in sys.argv[1:]:
		if "playlist?" in arg:
			playlist = Playlist(str(arg))
			pool.map(download_audio, playlist.video_urls)
		else:
			pool.submit(download_audio, arg)