import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600, 800))
clock = pygame.time.Clock()

class Racecar:
    def __init__(self, x, y):
        self.sprite = pygame.image.load("res/racecar_final.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (64, 64))

        self.rect = self.sprite.get_rect(center=(x, y))
        self.rect.inflate_ip(-36, -12)

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)
        pygame.draw.rect(screen, "red", self.rect, 1)

    def move(self, dx):
        self.rect.x += dx


class Tyre:
    def __init__(self, x, y):
        self.sprite = pygame.image.load("res/tyre_final.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (64, 64))

        self.rect = self.sprite.get_rect(center=(x, y))
        self.rect.inflate_ip(-16, -20)

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)
        pygame.draw.rect(screen, "blue", self.rect, 1)


racecar = Racecar(400, 300)
tyre = Tyre(600, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("white")

    tyre.draw(screen)
    racecar.draw(screen)

    if racecar.rect.colliderect(tyre.rect):
        racecar.rect.x = 0
    else:
        racecar.move(0.5)

    pygame.display.update()
    clock.tick(60)