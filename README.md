# youtubetomp3
Python program to download audio from YouTube video URLs

Wrapper around the [pytube](https://pytube.io/) library to download audio from YouTube videos.

Prefers the non-progressive `mp4` audio stream. If that is not available, tries `mp3`, and then whatever audio stream is available (perhaps `webm`).

Handles standard YouTube video URLs and playlist URLS; identifies playlists by the URL containing the text, "`playlist?`".

Downloads audio files 10 at a time; currently non-configurable.

Downloads file to the current working directory.

# Setup

## Install `python` version 3.
If on Windows, make sure to check the checkbox to install Python into the PATH.

## Install [pytube](https://pytube.io/en/latest/)
Once `python` is installed, open a command line/terminal and run the command `pip install pytube` 
(might be `pip3 install pytube`, depending on what's installed - if `pip3` is available, use that instead of `pip`).

# Usage

On Linux, Unix, and macOS, make the file executable (`chmod +x youtube2mp3.py`) and run it on the command line:
```
./youtube2mp3.py <YouTube URL> ...
```

On all operating systems, run it on the command line using `python3` (or `python`, depending on your installation - make sure you'e running Python 3 either way):
```
python3 youtube2mp3.py <YouTube URL> ...
```

# TODO
See [Issues](https://github.com/peterguy/youtubetomp3/issues)
