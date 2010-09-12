import pygame
from gameobjects.vector2 import Vector2

class Mobile(object):
    left_face = None
    right_face = None
    angle = 0.0
    facing = 'right'
    position = Vector2(0, 0)
    
    def face_left(self):
        self.facing = 'left'
    
    def face_right(self):
        self.facing = 'right'
    
    def render(self):
        if self.facing == 'right':
            face = self.right_face
        elif self.facing == 'left':
            face = self.left_face
        return face
    
    def set_position(self, pos):
        self.position = pos
    
    def get_position(self):
        y = self.position.y - (self.get_height()/4)*3
        return Vector2(self.position.x, y)
    
    def get_width(self):
        return self.right_face.get_width()
    
    def get_height(self):
        return self.right_face.get_height()

class Aduka(Mobile):
    
    aduka_right_img = 'resources/aduka/aduka_right.png'
    aduka_left_img = 'resources/aduka/aduka_left.png'
    
    def __init__(self):
        self.right_face = pygame.image.load(self.aduka_right_img).convert_alpha()
        self.left_face = pygame.image.load(self.aduka_left_img).convert_alpha()