import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600, 800), RESIZABLE)
pygame.display.set_caption("Car")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)


background_srfc = pygame.image.load("res/background2.png").convert_alpha()
background_srfc = pygame.transform.scale(background_srfc, (1600, 800))
text_srfc = font.render("Fitness: ", False, "Black")

tyre_srfc = pygame.image.load("res/tyre_final.png").convert_alpha()
tyre_srfc = pygame.transform.scale(tyre_srfc, (64, 64))
tyre_rect = tyre_srfc.get_rect(center=(600, 300))
tyre_rect.inflate_ip(-16 , -20)


racecar_srfc = pygame.image.load("res/racecar_final.png").convert_alpha()
racecar_srfc = pygame.transform.scale(racecar_srfc, (64, 64))
racecar_rect = racecar_srfc.get_rect(center=(400, 300))
racecar_rect.inflate_ip(-36, -12)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    
    screen.blit(background_srfc, (0,0))

    screen.blit(tyre_srfc, tyre_rect)
    pygame.draw.rect(screen, "red", racecar_rect, 1)

    pygame.draw.rect(screen, "blue", tyre_rect, 1)
    screen.blit(racecar_srfc, racecar_rect)
    if racecar_rect.colliderect(tyre_rect):
        racecar_rect.x = 0
    else:
        racecar_rect.x += 0.5
        
    screen.blit(text_srfc, (0, 0))

    print(racecar_rect.colliderect(tyre_rect))
    pygame.display.update()
    clock.tick(60)
