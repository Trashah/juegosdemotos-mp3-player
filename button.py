import pygame

class Button():
    #constructor
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

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("juegosdemotos mp3 player")

#mp3 variaables
mp3_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
stop_img = pygame.image.load("images/stop.png").convert_alpha
play_img = pygame.image.load("images/play.png").convert_alpha
next_img = pygame.image.load("images/next.png").convert_alpha
back_img = pygame.image.load("images/back.png").convert_alpha
quit_img = pygame.image.load("images/quit.png").convert_alpha
previous_img = pygame.image.load("images/previous.png").convert_alpha
settings_img = pygame.image.load("images/settings.png").convert_alpha

stop_button = Button(304, 125, stop_img, 1)
play_button = Button(297, 250, play_img, 1)
next_button = Button(336, 375, next_img, 1)
back_button = Button(226, 75, back_img, 1)
quit_button = Button(225, 200, quit_img, 1)
previous_button = Button(246, 325, previous_img, 1)
settings_button = Button(332, 450, settings_img, 1)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img (x, y))

#game loop
run = True