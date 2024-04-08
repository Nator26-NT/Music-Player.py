from tkinter import filedialog
from tkinter import *
import pygame
import os


root = Tk()
root.title("Music Player")
root.geometry("500x500")

pygame.mixer.init()

menuBar = Menu(root)
root.config(menu=menuBar)

songs = []
currentSong = ""
paused = False

def Load_Music():
    global currentSong
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songList.insert("end", song)
        
    songList.selection_set(0)
    currentSong = songs[songList.curselection()[0]]

def playmusic():
    global currentSong, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, currentSong))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pauseMusic():
    global paused
    pygame.mixer.music.pause()
    paused = True

def prev():
    global currentSong, paused
    try:
        songList.select_clear(0, END)
        songList.select_set(songs.index(currentSong) - 1)
        currentSong = songs[songList.curselection()[0]]
        playmusic()
    except:
        pass
    

def next():
    global currentSong, paused
    try:
        songList.select_clear(0, END)
        songList.select_set(songs.index(currentSong) + 1)
        currentSong = songs[songList.curselection()[0]]
        playmusic()
    except:
        pass

Organise_menu = Menu(menuBar, tearoff=False)
Organise_menu.add_command(label="Select Folder", command=Load_Music)
menuBar.add_cascade(label="Organise", menu=Organise_menu)

songList = Listbox(root, bg="gold", fg="black", width=100, height=15)
songList.pack()

playButton = PhotoImage(file="play.png")
pauseButton = PhotoImage(file="pause.png")
nextButton = PhotoImage(file="next.png")
previousButton = PhotoImage(file="prev.png")

control_frame  = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=playButton, borderwidth=0, command=playmusic) 
pause_btn = Button(control_frame, image=pauseButton, borderwidth=0, command=pauseMusic) 
next_btn = Button(control_frame, image=nextButton, borderwidth=0, command=next) 
prev_btn = Button(control_frame, image=previousButton, borderwidth=0, command=prev) 

play_btn.grid(row=0, column=2, padx=1, pady=2)
pause_btn.grid(row=0, column=1, padx=1, pady=2)
next_btn.grid(row=0, column=3, padx=1, pady=2)
prev_btn.grid(row=0, column=0, padx=1, pady=2)




root.mainloop()


