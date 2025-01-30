# Abre e reproduz um áudio MP3
import pygame
pygame.mixer.init()
pygame.mixer.music.load('04 - Body And Soul.mp3')
pygame.mixer.music.play()
x = input("Aperte Enter para finalizar o programa: ")
