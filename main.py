import pygame
from pygame import mixer
from tkinter import *
import tkinter as tk
from tkinter import filedialog

pygame.init()

#create pygame window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("juegosdemotos mp3")

menu_state = "main"

class ImageHandler:
    def __init__(self, x , y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Background(ImageHandler):
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Button(ImageHandler):
    def draw(self, surface):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
       
#create images
stop_img = pygame.image.load("images/stop.png").convert_alpha()
play_img = pygame.image.load("images/play.png").convert_alpha()
next_img = pygame.image.load("images/next.png").convert_alpha()
back_img = pygame.image.load("images/back.png").convert_alpha()
exit_img = pygame.image.load("images/exit.png").convert_alpha()
pause_img = pygame.image.load("images/pause.png").convert_alpha()
open_img = pygame.image.load("images/open.png").convert_alpha()
previous_img = pygame.image.load("images/previous.png").convert_alpha()
settings_img = pygame.image.load("images/settings.png").convert_alpha()
background1_img = pygame.image.load("images/background1.png").convert_alpha()
background2_img = pygame.image.load("images/background2.png").convert_alpha()

#create buttons
stop_button = Button(611, 464, stop_img, 0.37)
open_button = Button(618, 278, open_img, 0.4)
play_button = Button(611, 389, play_img, 0.18)
next_button = Button(336, 375, next_img, 1)
back_button = Button(226, 75, back_img, 1)
exit_button = Button(661, 464, exit_img, .19)
pause_button = Button(661, 389, pause_img, 0.18)
previous_button = Button(246, 325, previous_img, 1)
settings_button = Button(332, 450, settings_img, 1)

#create background
background1 = Background(0, 0, background1_img, 1)
background2 = Background(10, 50, background2_img, 0.23)

class MusicPlayer:
    def __init__(self):
        self.music_file = False
        self.music_name = None
        self.playing_state = False
        self.background_state = True
        self.paused = False

    def intro(self):
        mixer.init()
        mixer.music.load("audio files/en mp3 intro.mp3")
        mixer.music.play()

    def load(self):
            self.music_file = filedialog.askopenfilename()
            mixer.init()
            if self.music_file: mixer.music.load(self.music_file)
            pass

    def play(self):
        if self.music_file and not self.playing_state:
            if self.paused:
                mixer.music.unpause()
                self.paused = False
            else:
                mixer.music.play()
            self.playing_state = True
        pass

    def pause(self):
        if self.playing_state:
            mixer.music.pause()
            self.playing_state = False
            self.paused = True
        pass

    def stop(self):
        mixer.music.stop()
        self.music_file = None
        self.playing_state = False
        pass

    def changeLayout(self):
        pass

mp3 = MusicPlayer()

run = True

mp3.intro()
while run:
    
    screen.fill((255, 255, 255))
    if mp3.background_state:
        background1.draw(screen)
    else:
        background2.draw(screen)

    if open_button.draw(screen):
        mp3.stop()
        mp3.load()

    if play_button.draw(screen):
        mp3.play()

    if pause_button.draw(screen):
        mp3.pause()

    if stop_button.draw(screen):
        mp3.stop()

    if exit_button.draw(screen):
        run = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
    
    pygame.display.update()

pygame.quit()