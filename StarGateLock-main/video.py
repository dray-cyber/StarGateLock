import tkinter as tk, threading
import imageio
import pygame
import time
from PIL import Image, ImageTk

root = tk.Tk()
my_label = tk.Label(root)
my_label.pack()
video_name = "wormhole.mp4" #This is your video file path
video = imageio.get_reader(video_name)
pygame.mixer.init()
pygame.mixer.music.load("wormhole.mp3")
from moviepy.editor import *
import pygame

pygame.display.set_caption('Hello World!')

clip = VideoFileClip('wormhole.mp4')
clip.preview()

pygame.quit()
root.mainloop()
