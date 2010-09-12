import pygame
from pygame.locals import *
from gameobjects.vector2 import Vector2

floating_mountains = 'resources/floating_mountains.png'
vines = 'resources/vines.png'

background = pygame.image.load(floating_mountains).convert()
background_overlay = pygame.image.load(vines).convert_alpha()

def load_coordinates():
    f = open('coordinates.txt', 'r')
    lines = f.readlines()
    f.close()
    coordinates = []
    for l in lines:
        x, y = l.strip().split(",")
        coordinates.append(Vector2((int(x), int(y))))
    return coordinates 

def draw_background(screen):
    """draw base background"""
    screen.blit(background, (0, 0))
    screen.blit(background_overlay, (0, 0))