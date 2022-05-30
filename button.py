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

class Button():
    def __init__(self, x , y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

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

    #def hide(self, surface):


        



        

stop_img = pygame.image.load("images/stop.png").convert_alpha()
play_img = pygame.image.load("images/play.png").convert_alpha()
next_img = pygame.image.load("images/next.png").convert_alpha()
back_img = pygame.image.load("images/back.png").convert_alpha()
quit_img = pygame.image.load("images/quit.png").convert_alpha()
pause_img = pygame.image.load("images/pause.png").convert_alpha()
previous_img = pygame.image.load("images/previous.png").convert_alpha()
settings_img = pygame.image.load("images/settings.png").convert_alpha()

stop_button = Button(304, 125, stop_img, 1)
play_button = Button(300, 400, play_img, 0.5)
next_button = Button(336, 375, next_img, 1)
back_button = Button(226, 75, back_img, 1)
quit_button = Button(630, 500, quit_img, 1)
pause_button = Button(500, 400, pause_img, 0.5)
previous_button = Button(246, 325, previous_img, 1)
settings_button = Button(332, 450, settings_img, 1)

class MusicPlayer():
    def __init__(self):
        self.music_file = False
        self.playing_state = False

    def load(self):
            self.music_file = filedialog.askopenfilename()
            pass

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
            self.playing_state = True
        pass

    def pause(self):
        if self.playing_state:
            mixer.music.pause()
            self.playing_state = False
        else:
            mixer.music.unpause()
            self.playing_state = True
        pass

    def stop(self):
        pass

mp3 = MusicPlayer()
run = True
while run:
    
    screen.fill((52, 78, 91))

    if play_button.draw(screen):
        mp3.load()
        mp3.play()

    if pause_button.draw(screen):
        mp3.pause()

    if quit_button.draw(screen):
        run = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
    
    pygame.display.update()

pygame.quit()