
import pygame
import random

PURPLE =(81, 29, 67)
RED1 = (220, 37, 37)
RED2 = (144, 30, 62)
GREEN = (155, 192, 156)

from solution import manifold
start_grid = [row.copy() for row in manifold.grid]

pygame.init()

font_path = "PatrickHand-Regular.ttf"
font = pygame.font.Font(font_path, 30)

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Day 7: Laboratories")

running = True
clock = pygame.time.Clock()
row = 0
splits = 0
current = [0] * manifold.width
current[manifold.s_col] = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    spilts_text = f"Splits: {splits}"
    spilts_text = font.render(spilts_text, True, RED1)


    pygame.draw.rect(screen, "black", (45, 45, manifold.width*5, manifold.height*5))
    pygame.draw.rect(screen, (79, 32, 13), (350, 800-45, 100, 45))

    screen.blit(spilts_text, (20, 20))

    for i, r in enumerate(manifold.grid):

        for j, char in enumerate(r):
            if manifold.grid[i][j] == '.':
                continue
            elif char == manifold.grid[i][j] in ['S', 1]:
                pygame.draw.rect(screen, GREEN, (47 + j * 5, 45 + i * 5, 1, 5))


            else:
                if row < manifold.height:
                    pygame.draw.circle(screen, RED1, (47.5 + j * 5, 47 + i * 5), 3)
                else:
                    pygame.draw.circle(screen, random.choice([RED1, RED2, PURPLE]), (47.5 + j * 5, 47 + i * 5), 3)



    if row < manifold.height - 1:

        nxt = [0] * manifold.width
        nxt_row = manifold.grid[row + 1]

        for j in range(manifold.width):

            count = current[j]
            if count == 0:
                continue

            if nxt_row[j] != "^":
                nxt[j] += count
                manifold.grid[row + 1][j] = 1

            else:
                nxt[j - 1] += count
                nxt[j + 1] += count
                manifold.grid[row + 1][j - 1] = 1
                manifold.grid[row + 1][j+1] = 1
                splits += 1

        current = nxt


    timelines_text = f"Timelines: {sum(current)}"
    timelines_text = font.render(timelines_text, True, RED1)
    screen.blit(timelines_text, (20, 70))

    row += 1

    pygame.display.flip()
    clock.tick(15)

pygame.quit()
