# Included Libraries
from tkinter import *
from pygame import *
from tkinter.filedialog import askdirectory
import os

# Global Variables
songList = None

# mixer initialization
mixer.init()
# Take a music as input
def browseFiles():
    global songList
    if songList:
        songList.clear()
        label_song.config(text = 'Select a song')
    if play_listbox.get(ACTIVE):
        play_listbox.delete(0,END)
    directory = askdirectory()
    if not directory:
        return
    os.chdir(directory) #it permits to chenge the current dir
    songList = os.listdir() #it returns the list of files song
    lastSong = 0
    for song in songList:
        if '.mp3' in song:
            play_listbox.insert(lastSong, song)
            lastSong += 1
    songDisplay()

# song name display
def songDisplay():
    global songList
    label_song.config(text = play_listbox.get(ACTIVE))

# mixer play
def mixerPlay():
    global songList
    if not play_listbox.get(ACTIVE):
        return
    mixer.music.load(play_listbox.get(ACTIVE))
    var.set(play_listbox.get(ACTIVE))
    mixer.music.set_volume(0.5)
    mixer.music.play()
    songDisplay()

# mixer pause
def mixerPause():
    mixer.music.pause()

# mixer unpause
def mixerUnpause():
    mixer.music.unpause()

# mixer Stop
def mixerStop():
    mixer.music.stop()

# GUI init
root = Tk()
root.geometry("400x250")
root.resizable(0,0)
root.title("MP3 Player")
root.config(background = 'white')
var = StringVar()

# GUI Contain
label_songList = Label(root,
                       text = "Song List :",
                       fg = "black",
                       bg = "white")
label_song = Label(root,
                   text = "Select a Song",
                   fg = "black",
                   bg = "white")
button_explore = Button(root,
                        width = 15,
                        height = 2,
                        text = "Browse Files",
                        command = browseFiles)
button_play = Button(root,
                     width = 15,
                     height = 2,
                     text = "Play",
                     command = mixerPlay)
button_pause = Button(root,
                      width = 15,
                      height = 2,
                      text = "Pause",
                      command = mixerPause)
button_unpause = Button(root,
                        width = 15,
                        height = 2,
                        text = "Unpause",
                        command = mixerUnpause)
button_stop = Button(root,
                     width = 15,
                     height = 2,
                     text = "Stop",
                     command = mixerStop)
play_listbox = Listbox(root,
                       selectmode = 'single',
                       height = 12,
                       width = 30)

# Position
label_songList.pack(side = LEFT)
label_song.pack()
play_listbox.pack(side = LEFT)
button_explore.pack()
button_play.pack()
button_pause.pack()
button_unpause.pack()
button_stop.pack()

root.mainloop()
