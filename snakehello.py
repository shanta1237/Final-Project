import pygame
import random
from random import randint
import os

pygame.mixer.init()

pygame.init()



# Colors+
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
allo = (randint(0,255), randint(0,255), randint(0, 255))

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Background Image
bgimg = pygame.image.load("resources/images/background.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()


# Game Title
pygame.display.set_caption("Snkae game in pYgame")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial.ttf', 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        text_screen("Welcome to pygameSnakes", black, 260, 270)
        text_screen("Press Space Bar To Play", black, 232, 320)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('resources/music/bg_music_1.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)


