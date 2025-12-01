import pygame
import math

with open('input.txt', 'r') as f:
    r_words = [line.strip() for line in f.readlines()]

r = [int(x[1:]) if x[0] == "R" else -int(x[1:])for x in r_words]

pygame.init()

# Window
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Day 1: Secret Entrance!")

# Colors
BG = (62, 63, 41)
CIRCLE_COLOR = (125, 141, 134)
TEXT_COLOR = (241, 240, 228)
DOT_COLOR = (125, 141, 134)
POINTER_COLOR = (241, 240, 228)
CENTER_DOT_COLOR = (125, 141, 134)
RED = (228, 54, 54)

# Circle geometry
CENTER = (WIDTH // 2, HEIGHT // 2)
OUTER_RADIUS = 240
CENTER_DOT_RADIUS = 8

# Numbers
N = 100
STEP = 2 * math.pi / N
START_ANGLE = -math.pi / 2

# Font
font_path = "PatrickHand-Regular.ttf"
huge_font_size = 60
font_size = 18
huge_font = pygame.font.Font(font_path, huge_font_size)
font = pygame.font.Font(font_path, font_size)

clock = pygame.time.Clock()
running = True

# Pointer state
current_index = 50
rotation_num = 0
count = 0
password = 0

last_update_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- POINTER TIMING ---
    now = pygame.time.get_ticks()
    if rotation_num < len(r):
        if (now - last_update_time >= 20 and count !=0) or (now - last_update_time >= 500 and count == 0):
            if r[rotation_num] > 0:
                current_index = (current_index + 1) % N
            else:
                current_index = (current_index - 1) % N
            count += 1
            if count > abs(r[rotation_num]):
                count = 0
                rotation_num += 1
            last_update_time = now

            if current_index == 0:
                password += 1

    if current_index == 0:
        screen.fill(RED)
    else:
        screen.fill(BG)

    # Draw title


    if rotation_num == len(r):
        password_text = "The password is " + str(password)
    else:
        password_text = str(password)
    password_display = huge_font.render(password_text, True, TEXT_COLOR)
    password_rect = password_display.get_rect(center=(WIDTH / 2, 740))
    screen.blit(password_display, password_rect)

    if rotation_num < len(r):
        rotation_text = r_words[rotation_num]
        rotation_display = huge_font.render(rotation_text, True, TEXT_COLOR)
        rotation_rect = rotation_display.get_rect(center=(WIDTH / 2, 60))
        screen.blit(rotation_display, rotation_rect)

    else:
        title_text = "Secret Entrance to the North Pole!"
        title = huge_font.render(title_text, True, TEXT_COLOR)
        title_rect = title.get_rect(center=(WIDTH / 2, 60))
        screen.blit(title, title_rect)

    # Draw outer circle
    pygame.draw.circle(screen, CIRCLE_COLOR, CENTER, OUTER_RADIUS, 1)

    # Draw center dot
    pygame.draw.circle(screen, CENTER_DOT_COLOR, CENTER, CENTER_DOT_RADIUS)

    # Draw numbers
    for i in range(N):
        angle = START_ANGLE + i * STEP
        x = CENTER[0] + OUTER_RADIUS * math.cos(angle)
        y = CENTER[1] + OUTER_RADIUS * math.sin(angle)

        pygame.draw.circle(screen, DOT_COLOR, (int(x), int(y)), 3)

        if i % 5 == 0:
            text = str(i)
            surf = font.render(text, True, TEXT_COLOR)
            rect = surf.get_rect()

            # shift outward
            rect.center = (
                int(x + math.cos(angle) * 12),
                int(y + math.sin(angle) * 12)
            )

            screen.blit(surf, rect)

    # --- DRAW ANIMATED POINTER ---
    pointer_angle = START_ANGLE + current_index * STEP
    pointer_length = OUTER_RADIUS - 10

    px = CENTER[0] + pointer_length * math.cos(pointer_angle)
    py = CENTER[1] + pointer_length * math.sin(pointer_angle)

    pygame.draw.line(screen, POINTER_COLOR, CENTER, (px, py), 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()