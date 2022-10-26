# youtubetomp3
Python program to download audio from YouTube video URLs

Wrapper around the [pytube](https://pytube.io/) library to download audio from YouTube videos.

Prefers the non-progressive `mp4` audio stream. If that is not available, tries `mp3`, and then whatever audio stream is available (perhaps `webm`).

Handles standard YouTube video URLs and playlist URLS; identifies playlists by the URL containing the text, "`playlist?`".

Downloads audio files 10 at a time; currently non-configurable.

Downloads file to the current working directory.

# Usage

On Linux, Unix, and macOS, make the file executable (`chmod +x youtube2mp3.py`) and run it on the command line:
```
./youtube2mp3.py <YouTube URL> ...
```

On all operating systems, run it on the command line using `python3`:
```
python3 youtube2mp3.py <YouTube URL> ...
```

# TODO
- make sure that all playlist URLs are identified (they may not always contain "`playlist?`")
- Add commandline option to change how many files are downloaded at once
- Add commandline option for a target download directory