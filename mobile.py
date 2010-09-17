import pygame
from gameobjects.vector2 import Vector2

class Mobile(object):
    left_face = None
    right_face = None
    angle = 90.0
    facing = 'right'
    position = Vector2(0, 0)
    
    degree_pointer_img = 'resources/degree_pointer.png'
    
    def __init__(self):
        self.degree_pointer = pygame.image.load(self.degree_pointer_img).convert_alpha()
        self.angle_font = pygame.font.SysFont("arial", 10)
        self.angle_font.set_bold(True)
    
    def face_left(self):
        self.facing = 'left'
    
    def face_right(self):
        self.facing = 'right'
    
    def render(self, screen, rotation_direction):
        if self.facing == 'right':
            face = self.right_face
        elif self.facing == 'left':
            face = self.left_face
        pos = self.get_position()
        target_angle = self.angle + rotation_direction
        # rorate angle pointer
        rotated_pointer, rotated_pointer_pos = self._get_new_rotated_pos(
            face, pos, target_angle)
        screen.blit(rotated_pointer, rotated_pointer_pos)
        screen.blit(face, pos)
        
        angle_surface = self.angle_font.render(str(int(self.angle)), True, (127, 0, 108), (255, 255, 255))
        screen.blit(angle_surface, Vector2(pos.x, pos.y+(face.get_height()-angle_surface.get_height())))
        
    def _get_new_rotated_pos(self, face, base_pos, target_angle):
        if target_angle >= 0 and target_angle <=180:
            self.angle = target_angle
        elif target_angle >= 180:
            self.angle = 180.0
        elif target_angle <= 0:
            self.angle = 0.0
        rotated_pointer = pygame.transform.rotate(self.degree_pointer,
                                                  self.angle)
        w, h = rotated_pointer.get_size()
        rotated_pointer_pos = Vector2((base_pos.x-w/2) + (face.get_width()/2),
                                      (base_pos.y-h/2) + (face.get_height()/2))
        return (rotated_pointer, rotated_pointer_pos)
    
    def set_position(self, pos):
        self.position = pos
    
    def get_position(self):
        y = self.position.y - (self.get_height()/4)*3
        return Vector2(self.position.x, y)
    
    def get_width(self):
        return self.right_face.get_width()
    
    def get_height(self):
        return self.right_face.get_height()
    
    def set_angle(self, degree):
        self.angle = degree

class Aduka(Mobile):
    
    aduka_right_img = 'resources/aduka/aduka_right.png'
    aduka_left_img = 'resources/aduka/aduka_left.png'
    
    def __init__(self):
        self.right_face = pygame.image.load(self.aduka_right_img).convert_alpha()
        self.left_face = pygame.image.load(self.aduka_left_img).convert_alpha()
        super(Aduka, self).__init__()