import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption("Car")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)


background_srfc = pygame.image.load("res/background.png").convert_alpha()
background_srfc = pygame.transform.scale(background_srfc, (1600, 800))
text_srfc = font.render("Fitness: ", False, "Black")

tyre_srfc = pygame.image.load("res/tyre.png").convert_alpha()



racecar_srfc = pygame.image.load("res/racecar_sprite.png").convert_alpha()
racecar_srfc = pygame.transform.scale(racecar_srfc, (64, 64))

#racecar_xpos = 550
#racecar_ypos = 100

racecar_rect = racecar_srfc.get_rect(midbottom  = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    # screen.fill("white")
    screen.blit(background_srfc, (0,0))

    screen.blit(racecar_srfc, racecar_rect)
    racecar_rect.left += 1
    
        
    screen.blit(text_srfc, (0, 0))

    pygame.display.update()
    clock.tick(60)