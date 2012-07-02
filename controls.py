import pygame
from gameobjects.vector2 import Vector2

velocity_font = pygame.font.SysFont("arial", 10)
velocity_font.set_bold(True)

def draw_controls(screen, velocity):
    percentage = 100*velocity/296
    velocity_font_surface = velocity_font.render(str(float("%.2f" % percentage)), True, (127, 0, 108), (255, 255, 255))
    screen.blit(velocity_font_surface, Vector2(20, 394))
    pygame.draw.rect(screen, (127, 0, 108), (20, 407, 300, 20), 3) # red outline
    pygame.draw.rect(screen, (255, 255, 255), (22, 409, 296, 16)) # white outline fill
    pygame.draw.rect(screen, (255, 138, 0), (22, 409, velocity, 16))