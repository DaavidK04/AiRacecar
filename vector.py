import pygame
from sys import exit
import math

pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption("Car")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

#Hintergrund
background_srfc = pygame.image.load("res/background2.png").convert_alpha()
background_srfc = pygame.transform.scale(background_srfc, (1600, 800))
text_srfc = font.render("Fitness: ", False, "Black")

#Reifen (brauch ich eig nicht)
tyre_srfc = pygame.image.load("res/tyre_final.png").convert_alpha()
tyre_srfc = pygame.transform.scale(tyre_srfc, (64, 64))
tyre_rect = tyre_srfc.get_rect(center=(600, 300))
tyre_rect.inflate_ip(-16 , -20)

#Auto
racecar_srfc = pygame.image.load("res/racecar_right.png").convert_alpha()
racecar_rect = racecar_srfc.get_rect(center=(400, 650))

speed = 4        # Vorwärtsgeschwindigkeit
rot_speed = 3    # Max Drehgeschwindigkeit pro Frame (Grad)

car_angle = 0    # Aktueller Winkel des Autos

game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if not game_over:
        #Bewegungsvektor berechnen
        move_x = 0
        move_y = 0
        if keys[pygame.K_RIGHT]:
            move_x += 1
        if keys[pygame.K_LEFT]:
            move_x -= 1
        if keys[pygame.K_UP]:
            move_y -= 1
        if keys[pygame.K_DOWN]:
            move_y += 1

        if move_x != 0 or move_y != 0:
            length = math.hypot(move_x, move_y)
            move_x /= length
            move_y /= length

            #Zielwinkel berechnen
            target_angle = math.degrees(math.atan2(-move_y, move_x))

            #Winkeldifferenz berechnen
            diff = (target_angle - car_angle + 180) % 360 - 180

            #Winkel schrittweise ändern
            if diff > rot_speed:
                diff = rot_speed
            elif diff < -rot_speed:
                diff = -rot_speed
            car_angle += diff
            car_angle %= 360

            #Auto bewegen
            rad = math.radians(car_angle)
            racecar_rect.x += math.cos(rad) * speed
            racecar_rect.y -= math.sin(rad) * speed  # -sin wegen pygame y-Achse

        #Kollision mit der Strecke überprüfen (schwarz = Straße)
        x, y = racecar_rect.center
        #Clamp, damit wir keine IndexError bekommen
        x = max(0, min(screen.get_width()-1, int(x)))
        y = max(0, min(screen.get_height()-1, int(y)))
        pixel_color = background_srfc.get_at((x, y))[:3]

        if pixel_color != (0, 0, 0):  #alles was nicht schwarz ist -> offroad
            game_over = True
            print("Game Over! Auto ist von der Strecke abgekommen.")

    #Auto rendern
    rotated_car = pygame.transform.rotate(racecar_srfc, car_angle)
    rotated_rect = rotated_car.get_rect(center=racecar_rect.center)

    #Bildschirm zeichnen
    screen.blit(background_srfc, (0,0))
    screen.blit(tyre_srfc, tyre_rect)
    pygame.draw.rect(screen, "blue", tyre_rect, 1)
    pygame.draw.rect(screen, "red", rotated_rect, 1)
    screen.blit(rotated_car, rotated_rect)
    screen.blit(text_srfc, (0, 0))

    pygame.display.update()
    clock.tick(60)
