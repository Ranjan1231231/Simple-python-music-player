import random
import tkinter as tk
from tkinter import ttk
import pygame
import os
from tkinter import filedialog


root = tk.Tk()
root.title("MUSIC PLAYER")
pygame.init()
pygame.mixer.init()

folder_path = ""
song_list = []
current_song_index = 0
shuffle_on = False
repeat_on = False


def play_pause():
    global current_song_index
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(folder_path + "/" +song_list[current_song_index])
        pygame.mixer.music.play()
        play_button.config(text="Pause")
    else:
        pygame.mixer.music.pause()
        play_button.config(text="Play")
song_label = tk.Label(root, text="No song selected")
# ...

def update_song_label():
    if song_list:
        song_label.config(text=song_list[current_song_index])
    else:
        song_label.config(text="No song selected")


def next_song():
    global current_song_index
    if shuffle_var.get():
        current_song_index = random.randint(0, len(song_list) - 1)
    elif repeat_var.get():
        current_song_index = current_song_index
    else:
        current_song_index += 1
        if current_song_index >= len(song_list):
            current_song_index = 0
    pygame.mixer.music.load(folder_path + "/" +song_list[current_song_index])
    pygame.mixer.music.play()
    song_label.config(text=song_list[current_song_index])
    update_song_label()




def prev_song():
    global current_song_index
    current_song_index -= 1
    if current_song_index < 0:
        current_song_index = len(song_list) - 1
    pygame.mixer.music.load(folder_path + "/" +song_list[current_song_index])
    pygame.mixer.music.play()
    song_label.config(text=song_list[current_song_index])
    update_song_label()

def set_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

def open_folder():
    global folder_path
    global song_list
    folder_path = filedialog.askdirectory()
    song_list = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]
    if song_list:
        song_label.config(text=song_list[current_song_index])
    update_song_label()


open_button = ttk.Button(root, text="Open", command=open_folder)
open_button.grid(row=0, column=0, padx=5, pady=5)

song_label.grid(row=1, column=0, columnspan=6, padx=5, pady=5)

time_slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", value=0)
time_slider.grid(row=2, column=2, padx=10, pady=5)

prev_button = ttk.Button(root, text="Prev", command=prev_song)
prev_button.grid(row=5, column=0, padx=5, pady=5)

play_button = ttk.Button(root, text="Play", command=play_pause)
play_button.grid(row=5, column=1, padx=5, pady=5)

next_button = ttk.Button(root, text="Next", command=next_song)
next_button.grid(row=5, column=2, padx=5, pady=5)

volume_slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=set_volume, value=60)
volume_slider.set(60)
volume_slider.grid(row=5, column=3, columnspan=2, padx=5, pady=5)







repeat_var = tk.BooleanVar()
repeat_var.set(False)
repeat_button = ttk.Checkbutton(root, text="Repeat", variable=repeat_var)
repeat_button.grid(row=6, column=4, padx=5, pady=5)



shuffle_var = tk.BooleanVar()
shuffle_var.set(False)
shuffle_button = ttk.Checkbutton(root, text="Shuffle", variable=shuffle_var)
shuffle_button.grid(row=6, column=3, padx=5, pady=5)




root.mainloop()
