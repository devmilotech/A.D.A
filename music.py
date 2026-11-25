import pygame
import os

os.system("cls")

pygame.mixer.init()

def Play(file="song.mp3"):
    if not os.path.exists(file):
        return

    try:
        pygame.mixer.music.load(file)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
    except pygame.error as e:
        print(e)

def Stop():
    pygame.mixer.music.stop()
