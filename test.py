import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption("Car")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

race_car = pygame.image.load("res/racecar_sprite.png").convert_alpha()
race_car = pygame.transform.scale(race_car, (64, 64))
background = pygame.image.load("res/background.png").convert_alpha()
text_surface = font.render("Fitness: ", False, "Black")

racecar_xpos = 550

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("white")
    #screen.blit(background, (0,0))

    if racecar_xpos > 1660:
        racecar_xpos = 0
    racecar_xpos += 3
    screen.blit(race_car,(racecar_xpos,100))
        
    screen.blit(text_surface, (0, 0))

    pygame.display.update()
    clock.tick(60)