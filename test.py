import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600, 800))
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


racecar_up_srfc = pygame.image.load("res/racecar_final.png").convert_alpha()
racecar_right_srfc = pygame.image.load("res/racecar_right.png").convert_alpha()
racecar_down_srfc = pygame.image.load("res/racecar_down.png").convert_alpha()
racecar_left_srfc = pygame.image.load("res/racecar_left.png").convert_alpha()

car_sprites = {
    "up": (racecar_up_srfc, (-36, -12)),     
    "right": (racecar_right_srfc, (-12, -36)), 
    "down": (racecar_down_srfc, (-36, -12)),
    "left": (racecar_left_srfc, (-12, -36)),
    "schraeg": (pygame.transform.rotate(racecar_right_srfc, -20), (-12, -36))
}

direction = "right"
current_srfc, hitbox_adjust = car_sprites[direction]
racecar_rect = current_srfc.get_rect(center=(400, 300))
racecar_rect.inflate_ip(*hitbox_adjust)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        direction = "right"
        racecar_rect.x += 2
    if keys[pygame.K_LEFT]:
        direction = "left"
        racecar_rect.x -= 2
    if keys[pygame.K_UP]:
        direction = "up"
        racecar_rect.y -= 2
    if keys[pygame.K_DOWN]:
        direction = "down"
        racecar_rect.y += 2
    if keys[pygame.K_1]:
        pygame.transform.rotate(current_srfc, 2)

    #current_srfc, hitbox_adjust = car_sprites[direction]

    center = racecar_rect.center
    racecar_rect = current_srfc.get_rect(center=center)
    racecar_rect.inflate_ip(*hitbox_adjust)

    screen.blit(background_srfc, (0,0))
    screen.blit(tyre_srfc, tyre_rect)

    pygame.draw.rect(screen, "blue", tyre_rect, 1)
    pygame.draw.rect(screen, "red", racecar_rect, 1)

    screen.blit(current_srfc, racecar_rect)
    screen.blit(text_srfc, (0, 0))

    print(racecar_rect.colliderect(tyre_rect))


    pygame.display.update()
    clock.tick(60)
