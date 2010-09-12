import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
from math import *
from screen import *
from utils import load_coordinates, draw_background
from mobile import Aduka

coordinates = load_coordinates()
aduka = Aduka()
movement_index = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT] and coordinates[movement_index].x > 0:
        movement_index -= 1
        aduka.face_left()
    elif pressed_keys[K_RIGHT] and coordinates[movement_index].x <= (SCREEN_SIZE[0] - aduka.get_width()):
        movement_index += 1
        aduka.face_right()
    
    aduka.set_position(coordinates[movement_index])
    
    draw_background(screen)
    screen.blit(aduka.render(), aduka.get_position())
    
    pygame.display.update()