from tkinter import *
import pygame

root = Tk()
root.title('Max Lake - Tracks')
root.geometry("500x600")

pygame.mixer.init()
pygame.mixer.music.set_volume(0.4)

def play():
    pygame.mixer.music.load("Max Lake - Minimix.mp3")

    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

my_button = Button(root, text="Max Lake - DJ Mix", font=("Helvetica", 16), command=play)
my_button.pack(pady=20)

stop_button = Button(root, text="Stop", command=stop)
stop_button.pack(pady=20)




def play1():
    pygame.mixer.music.load("colors_demo.mp3")
    pygame.mixer.music.play(loops=0)

def stop1():
    pygame.mixer.music.stop()

my_button1 = Button(root, text="Max Lake - Colours of Your Heart", font=("Helvetica", 16),  command=play1)
my_button1.pack(pady=20)

stop_button1 = Button(root, text="Stop", command=stop1)
stop_button1.pack(pady=20)




def play2():
    pygame.mixer.music.load("wake_demo.mp3")
    pygame.mixer.music.play(loops=0)

def stop2():
    pygame.mixer.music.stop()

my_button2 = Button(root, text="Max Lake & JULYO - Wanna Wake Up", font=("Helvetica", 16), command=play2)
my_button2.pack(pady=20)

stop_button2 = Button(root, text="Stop", command=stop2)
stop_button2.pack(pady=20)




def play3():
    pygame.mixer.music.load("star_demo.mp3")
    pygame.mixer.music.play(loops=0)

def stop3():
    pygame.mixer.music.stop()

my_button3 = Button(root, text="Max Lake - The Star is Born", font=("Helvetica", 16), command=play3)
my_button3.pack(pady=20)

stop_button3 = Button(root, text="Stop", command=stop3)
stop_button3.pack(pady=20)



root.mainloop()