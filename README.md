# youtubetomp3
Python program to download audio from YouTube video URLs

Wrapper around the [pytubefix](https://github.com/JuanBindez/pytubefix) library to download audio from YouTube videos.

Prefers the non-progressive `mp4` audio stream. If that is not available, tries `mp3`, and then whatever audio stream is available (perhaps `webm`).

Handles standard YouTube video URLs and playlist URLS; identifies playlists by the URL containing the text, "`playlist?`".

Downloads audio files 10 at a time; currently non-configurable.

Downloads file to the current working directory.

# Setup

## Install `python` version 3.
If on Windows, make sure to check the checkbox to install Python into the PATH.

## Setup environment (once)
```
python3 -m venv .venv
```

## activate environment (each new terminal)
```
source .venv/bin/activate
```

## Install [pytubefix](https://github.com/JuanBindez/pytubefix) and pyinstaller (to make executable)
```
pip install pytubefix pyinstaller
```

## Generate executable
```
python -m PyInstaller --onefile --name youtube2mp3 youtube2mp3.py
```

## Copy executable into PATH
Depends on your setup; using `~/.local/bin` here
```
cp dist/youtube2mp3 ~/.local/bin
```

# Usage

On Linux, Unix, and macOS, use the executable:
```
youtube2mp3 <YouTube URL> ...
```

On all operating systems, run it on the command line using `python`:
```
python youtube2mp3.py <YouTube URL> ...
```

Use `youtube2mp3 --help` (or `python youtube2mp3.py --help`) for usage information.
Quote URLs, especially when they contain `&`:
```
youtube2mp3 "https://www.youtube.com/watch?v=VIDEO_ID"
```

Note that although the name of this project is "youtube2mp3", it downloads audio in mp4 by preference, mp3 if no mp4, and then whatever format is available - the program does not convert it to mp3.
Exit status is `0` on success, `1` if any download or playlist fails, and `2` for invalid command-line arguments (including supplying no URLs).

# TODO
See [Issues](https://github.com/peterguy/youtubetomp3/issues)
