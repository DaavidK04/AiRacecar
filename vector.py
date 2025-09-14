import pygame
from sys import exit
import math
from pygame.math import Vector2

pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption("Car")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

# Hintergrund
background_srfc = pygame.image.load("res/background2.png").convert_alpha()
background_srfc = pygame.transform.scale(background_srfc, (1600, 800))
text_srfc = font.render("Fitness: ", False, "Black")

# Auto
racecar_srfc = pygame.image.load("res/racecar_right.png").convert_alpha()

# Position (float) = Center des Autos in Bildschirmkoordinaten
pos = Vector2(400.0, 650.0)

# 👇 Hier deine festen Werte eintragen (relativ zur Rect-Mitte!)
car_offset = Vector2(-7, -18)  # Beispiel: 12px rechts, 8px nach oben

speed = 4.0
rot_speed = 3.0
car_angle = 0.0  # Grad
game_over = False

def rotate_screen_vector(v: Vector2, angle_deg: float) -> Vector2:
    """Dreht Vektor v (in Screen-Koordinaten, y nach unten) um angle_deg Grad."""
    rad = math.radians(angle_deg)
    c = math.cos(rad)
    s = math.sin(rad)
    rx = v.x * c + v.y * s
    ry = v.y * c - v.x * s
    return Vector2(rx, ry)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if not game_over:
        move_x = move_y = 0
        if keys[pygame.K_RIGHT]:
            move_x += 1
        if keys[pygame.K_LEFT]:
            move_x -= 1
        if keys[pygame.K_UP]:
            move_y -= 1
        if keys[pygame.K_DOWN]:
            move_y += 1

        if move_x or move_y:
            length = math.hypot(move_x, move_y)
            move_x /= length
            move_y /= length

            target_angle = math.degrees(math.atan2(-move_y, move_x))
            diff = (target_angle - car_angle + 180) % 360 - 180

            if diff > rot_speed:
                diff = rot_speed
            elif diff < -rot_speed:
                diff = -rot_speed
            car_angle += diff
            car_angle %= 360

            rad = math.radians(car_angle)
            pos.x += math.cos(rad) * speed
            pos.y -= math.sin(rad) * speed  # Minus, weil screen-y nach unten wächst

        # Kollisionspunkt = pos + rotierten Offset
        rotated_offset = rotate_screen_vector(car_offset, car_angle)
        collision_point = pos + rotated_offset

        # Kollision prüfen
        cx, cy = int(round(collision_point.x)), int(round(collision_point.y))
        cx = max(0, min(screen.get_width() - 1, cx))
        cy = max(0, min(screen.get_height() - 1, cy))
        pixel_color = background_srfc.get_at((cx, cy))[:3]
        if pixel_color != (0, 0, 0):
            game_over = True
            print("Game Over! Auto ist von der Strecke abgekommen. Pixel:", pixel_color, "Pos:", (cx, cy))

    # Rendern
    rotated_car = pygame.transform.rotate(racecar_srfc, car_angle)
    rotated_rect = rotated_car.get_rect(center=(int(pos.x), int(pos.y)))

    screen.blit(background_srfc, (0, 0))
    screen.blit(rotated_car, rotated_rect)

    # Debug: Center + Kollisionspunkt anzeigen
    pygame.draw.circle(screen, "yellow", (int(pos.x), int(pos.y)), 4)  # Rect-Mitte
    pygame.draw.circle(screen, "red", (int(round(collision_point.x)), int(round(collision_point.y))), 5)  # Kollisionspunkt

    screen.blit(text_srfc, (0, 0))
    pygame.display.update()
    clock.tick(60)
