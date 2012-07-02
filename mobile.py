import math
import pygame
from gameobjects.vector2 import Vector2
from utils import blit_alpha


class Mobile(object):
    left_face = None
    right_face = None
    angle = 90.0
    facing = 'right'
    position = Vector2(0, 0)
    gravity = 9.8
    dt = 0.07  # difference in time
    is_dead = False
    degree_pointer_img = 'resources/degree_pointer.png'
    fireball = 'resources/fireball.png'

    velocity = 0
    seconds = 0

    width = 47
    height = 45
    opacity = 250

    def __init__(self):
        self.degree_pointer = pygame.image.load(self.degree_pointer_img).convert_alpha()
        self.angle_font = pygame.font.SysFont("arial", 10)
        self.angle_font.set_bold(True)
        self.mobile_fire = pygame.image.load(self.fireball).convert_alpha()

    def face_left(self):
        self.facing = 'left'

    def face_right(self):
        self.facing = 'right'

    def render(self, screen, rotation_direction, enemy):
        if self.facing == 'right':
            face = self.right_face
        elif self.facing == 'left':
            face = self.left_face
        pos = self.get_position()
        target_angle = self.angle + rotation_direction

        if self.is_dead and self.opacity > 0:
                position = self.get_position()
                self.opacity = self.opacity - 5
                blit_alpha(screen, face, (position.x, position.y), self.opacity)
        elif not self.is_dead:
            # rotate angle pointer
            rotated_pointer, rotated_pointer_pos = self._get_new_rotated_pos(
                face, pos, target_angle)
            screen.blit(rotated_pointer, rotated_pointer_pos)
            screen.blit(face, pos)

            angle_surface = self.angle_font.render(
                str(int(self.angle)),
                True,
                (127, 0, 108),
                (255, 255, 255))
            position = Vector2(
                pos.x, pos.y + (face.get_height() - angle_surface.get_height()))
            screen.blit(angle_surface, position)

        # check for firing
        if self.velocity != 0:
            angle = self.angle * (math.pi / 180)  # converted to radians
            VelocityY = self.velocity * math.sin(angle)
            VelocityX = self.velocity * math.cos(angle)

            position = self.get_position()
            initial_x, initial_y = position.x, position.y

            self.seconds += self.dt
            ball_x = initial_x + (VelocityX * self.seconds)
            ball_y = initial_y - (VelocityY * self.seconds - .5 * self.gravity * self.seconds ** 2)
            screen.blit(self.mobile_fire, (ball_x, ball_y))

            # check if we hit something
            if enemy:
                enemy_pos = enemy.get_position()
                hit = (ball_x + self.width > enemy_pos.x and
                    ball_x < enemy_pos.x + enemy.width and
                    ball_y + self.height > enemy_pos.y and
                    ball_y < enemy_pos.y + enemy.height)

                if hit and not enemy.is_dead:
                    enemy.is_dead = True

            # reset velocity and seconds when we're outside the window
            if ball_y >= initial_y:
                self.velocity = 0
                self.seconds = 0

    def _get_new_rotated_pos(self, face, base_pos, target_angle):
        if target_angle >= 20 and target_angle <= 160:
            self.angle = target_angle
        elif target_angle >= 160:
            self.angle = 160.0
        elif target_angle <= 20:
            self.angle = 20.0
        rotated_pointer = pygame.transform.rotate(self.degree_pointer,
                                                  self.angle)
        w, h = rotated_pointer.get_size()
        rotated_pointer_pos = Vector2((base_pos.x - w / 2) + (face.get_width() / 2),
                                      (base_pos.y - h / 2) + (face.get_height() / 2))
        return (rotated_pointer, rotated_pointer_pos)

    def set_position(self, pos):
        self.position = pos

    def get_position(self):
        y = self.position.y - (self.get_height() / 4) * 3
        return Vector2(self.position.x, y)

    def get_width(self):
        return self.right_face.get_width()

    def get_height(self):
        return self.right_face.get_height()

    def set_angle(self, degree):
        self.angle = degree

    def fire(self, velocity_percentage):
        self.velocity = velocity_percentage


class Aduka(Mobile):

    aduka_right_img = 'resources/aduka/aduka_right.png'
    aduka_left_img = 'resources/aduka/aduka_left.png'

    def __init__(self):
        self.right_face = pygame.image.load(self.aduka_right_img).convert_alpha()
        self.left_face = pygame.image.load(self.aduka_left_img).convert_alpha()
        super(Aduka, self).__init__()
