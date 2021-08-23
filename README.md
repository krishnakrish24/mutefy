# Mutefy v1.0
 Mute Spotify Ads on Desktop.
 Created using Python with Spotify API,
 GUI - tkinter

This application mutes Spotify when it detects an ad playing and gives the user the option to play a random song that is available locally.

## Installation and Usage
1. Login to Spotify Developer Console using https://developer.spotify.com/dashboard/
2. Click 'Create an app' and key in the inputs as required.
3. Copy your client id and client secret once the app is created.
4. Clone this repository and open the mutefy.py file.
5. Replace the copied values in the appropriate variables in the mutefy.py file.
6. Make sure that you have all the dependencies installed in your system. For the list of dependencies, check the [Dependencies](#dependencies) section
8. Save the file and run the file from the command line using the python command:
`python mutefy.py`

## Dependencies
- psutil
- pygetwindow
- pycaw
- pygame
- spotipy
- tkinter

If you do not have these dependencies installed, install them using the command line.

`pip install psutil pygetwindow pycaw pygame spotipy tkinter`

## GUI
![Mutefy v1.0 GUI](https://github.com/krishnakrish24/mutefy/blob/7cb732d80ea9078ee2667610bfa2cf653cc5b9b0/Mutefy%20v1_0.png)
- The Open Spotify button opens the Spotify application.
- You can select the folder containing the music you want to play when Spotify is muted using the Browse button. Please ensure that the folder contains only mp3 files.
- The START button starts the application. The status then changes from Stopped... to Running!
- The current playing song name, its artist and the album are displayed at the bottom.
