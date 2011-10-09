import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
from math import *
from screen import *
from utils import load_coordinates, draw_background
from mobile import Aduka
from controls import draw_controls

coordinates = load_coordinates()
aduka = Aduka()
movement_index = 0
velocity = 0.0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            velocity = 0.0
        elif event.type == KEYUP and event.key == K_SPACE:
            aduka.fire(velocity)
    
    pressed_keys = pygame.key.get_pressed()
    
    rotation_direction = 0.0
    
    if pressed_keys[K_LEFT] and coordinates[movement_index].x > 0:
        movement_index -= 1
        aduka.face_left()
    elif pressed_keys[K_RIGHT] and coordinates[movement_index].x <= (SCREEN_SIZE[0] - aduka.get_width()):
        movement_index += 1
        aduka.face_right()
    elif pressed_keys[K_UP]:
        rotation_direction = +1.0
    elif pressed_keys[K_DOWN]:
        rotation_direction = -1.0
    elif pressed_keys[K_SPACE]:
        if (velocity + 1) <= 296:
            velocity += 1
    
    aduka.set_position(coordinates[movement_index])
    
    draw_background(screen)
    aduka.render(screen, rotation_direction)
    draw_controls(screen, velocity)
    pygame.display.update()
