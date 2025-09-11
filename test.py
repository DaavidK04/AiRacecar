import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption("Car")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)


background = pygame.image.load("res/background.png").convert_alpha()
background = pygame.transform.scale(background, (1600, 800))
text_surface = font.render("Fitness: ", False, "Black")


race_car = pygame.image.load("res/racecar_sprite.png").convert_alpha()
race_car = pygame.transform.scale(race_car, (64, 64))

#racecar_xpos = 550
#racecar_ypos = 100

racecar_rect = race_car.get_rect(midbottom  = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    # screen.fill("white")
    screen.blit(background, (0,0))

    screen.blit(race_car, racecar_rect)
    racecar_rect.left += 1
    
        
    screen.blit(text_surface, (0, 0))

    pygame.display.update()
    clock.tick(60)