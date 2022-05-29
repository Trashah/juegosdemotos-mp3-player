import pygame
from tkinter import *
import tkinter as tk
from tkinter import filedialog

class Button():
    def _init_(self, x , y, image, scale):
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
        if self.rect.collidepoint():
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

stop_img = pygame.image.load("images/stop.png").convert_alpha
play_img = pygame.image.load("images/play.png").convert_alpha
next_img = pygame.image.load("images/next.png").convert_alpha
back_img = pygame.image.load("images/back.png").convert_alpha
quit_img = pygame.image.load("images/quit.png").convert_alpha
previous_img = pygame.image.load("images/previous.png").convert_alpha
settings_img = pygame.image.load("images/settings.png").convert_alpha

class MusicPlayer():
    def _init_(self, win):
        #create Tkinter window
        win.geometry("200x200")
        win.title("juegosdemotos mp3 player")
        win.resizable(0, 0)

        
        stop_button = Button(304, 125, stop_img, 1)
        play_button = Button(297, 250, play_img, 1)
        next_button = Button(336, 375, next_img, 1)
        back_button = Button(226, 75, back_img, 1)
        quit_button = Button(225, 200, quit_img, 1)
        previous_button = Button(246, 325, previous_img, 1)
        settings_button = Button(332, 450, settings_img, 1)

    def load(self):
        pass

    def play(self):
        pass

    def pause(self):
        pass

    def stop(self):
        pass

root = Tk()
MusicPlayer(root)

root.mainloop()
