from cmath import rect

import pygame
import random
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72
pygame.init()
background_image = pygame.image.load("background.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT)
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(
            pygame.Color('dogerblue'))
        pygame.draw.rect(self.image, pygame.Color('black'), pygame.Rect(0, 0, 50, 50), 2)
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0
        )
        self.rect.y = max(
            min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0
        )
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Movement")
all_sprites = pygame.sprite.Group()
sprite1 = Sprite(pygame.Color('black'), 20, 30)
sprite1.rect.x, sprite1.rect.y = (
    0,SCREEN_HEIGHT - sprite1.rect.height
), random.randint(0, SCREEN_WIDTH - sprite1.rect.width)
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color('black'), 20, 30)
sprite2.rect.x, sprite2.rect.y = (