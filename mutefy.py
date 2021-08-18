import os
import tkinter as tk
from tkinter import filedialog
import psutil
import pygetwindow as gw
import spotipy
import spotipy.util as util 
import time
from pycaw.pycaw import AudioUtilities
from threading import Thread
import random
from pygame import mixer

username = 'Client Username Here'
cid = 'Client ID Here'
secret = 'Client Secret ID Here'
accessscope='user-read-currently-playing user-modify-playback-state'
redirectURI='Your redirectURI'

def setupobj(username,scope,clientid,clientsecret,redirect_uri):
    token = util.prompt_for_user_token(username,scope,clientid,clientsecret,redirect_uri)
    return spotipy.Spotify(auth=token)

def openspotify():
    try:
        if 'Spotify' in (p.name() for p in psutil.process_iter()):  
            s = gw.getWindowsWithTitle('Spotify')[0] 
            s.activate()
        else:
            os.system("Spotify")
    except:
        tk.messagebox.showinfo("Welcome to Mutefy",  "Spotify is not installed! Please install Spotify!") 

def checkads():
    global sobj
    sts.set("Running!")
    txt.config(fg='green')
    try:
        trackInfo = sobj.current_user_playing_track()
    except:
        print('Token Expired!')
        sobj = setupobj(username,accessscope,cid,secret,redirectURI)
        trackInfo = sobj.current_user_playing_track()
    
    try:
        if trackInfo['currently_playing_type'] == 'ad':
            mutefy(True)
            global flag
            if flag:
                playmusic()
                flag=False
        else:
            mixer.music.pause()
            flag=True
            mutefy(False)
    except TypeError:
        pass

mixer.init()

def playmusic():
    try:
        mixer.music.load(file) 
        mixer.music.set_volume(0.7)
        mixer.music.play()
    except:
        pass

def mutefy(mute):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        vol = session.SimpleAudioVolume
        if session.Process and session.Process.name() == 'Spotify.exe':
            if mute:
                vol.SetMute(1,None) 
            else:
                vol.SetMute(0,None)

def threading():
    t1=Thread(target=work)
    t1.start()

def supdate():
    ct=gettrack()
    ca=getartist()
    calbum=getalbum()
    tracks.set(ct)
    artist.set(ca)
    album.set(calbum)
    win.update()

def work():
    global flag
    flag=True
    while True:
        checkads()
        try:
            supdate()
            win.update()
        except:
            break
        time.sleep(0.1)

def gettrack():
    track = sobj.current_user_playing_track()
    try:
        trackn=track['item']['name']
    except:
        trackn="Ad or Stopped!"
    name = "Now Playing: " + trackn
    return name

def getartist():
    gartist = sobj.current_user_playing_track()
    artists=[]   
    try:
        artistlen = len(gartist['item']['artists'])
        for i in range(0,artistlen):
            artists.append(gartist['item']['artists'][i]['name']) 
        artistn = ', '.join(artists)
    except:
        artistn="N/A"
    aname = "Artist: " + artistn
    return aname

def getalbum():
    galbum = sobj.current_user_playing_track()
    try:
        albumn=galbum['item']['album']['name']
    except:
        albumn="N/A"
    albumname = "Album: " + albumn
    return albumname

def select():
    global file
    path = tk.filedialog.askdirectory()
    fold = "Selected Folder: " + path
    folder.set(fold)
    file = os.path.join(path, random.choice(os.listdir(path)))


win=tk.Tk()
win.title('Mutefy')
win.geometry('360x280')
win.iconphoto(False,tk.PhotoImage(file='spotify.png'))

sobj = setupobj(username,accessscope,cid,secret,redirectURI)
tk.Label(win, text='Mutefy v1.0').pack()
tk.Button(win, text='Open Spotify', width=20, pady=5, command=openspotify).pack()
tk.Label(win, text='').pack()

tk.Label(win, text='Select the folder to play from when Spotify is muted').pack()
frame=tk.Frame()
frame.pack()
tk.Button(frame, text='Browse', width=8, pady=2, command=select).grid(row=0,column=0)
folder=tk.StringVar()
folder.set("Current Folder: None")
tk.Label(frame, textvariable=folder).grid(row=0,column=1)
tk.Label(win, text='').pack()

tk.Button(win, text='START' , bg='green', fg='white', width=10, pady=5, command=work).pack()
sts=tk.StringVar()
sts.set("Stopped...")
txt=tk.Label(win, textvariable=sts,fg='red',pady=5)
txt.pack()

tracks=tk.StringVar()
tracks.set(gettrack())
tk.Label(win, textvariable=tracks,pady=1).pack()
artist=tk.StringVar()
artist.set(getartist())
tk.Label(win, textvariable=artist,pady=1).pack()
album=tk.StringVar()
album.set(getalbum())
tk.Label(win, textvariable=album,pady=1).pack()
win.mainloop()