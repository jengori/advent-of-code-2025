import pygame

GRID_COLOR = (54, 1, 133)

from solution import Grid

with open("input.txt") as f:
    lst_ = [[char for char in line] for line in f.read().splitlines()]

grid = Grid(lst_)
start_rolls = len(grid.rolls)

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Day 4: Printing Department")

font_path = "PatrickHand-Regular.ttf"
font = pygame.font.Font(font_path, 16)

running = True
clock = pygame.time.Clock()
row = 1
rolls_removed = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((54, 1, 133))

    pygame.draw.rect(screen, GRID_COLOR, (50, 50, grid.width*5, grid.height*5))

    for i, r in enumerate(grid.rows):
        for j, char in enumerate(r):
            if grid.rows[i][j] == "@":
                pygame.draw.circle(screen, (244, 179, 66), (52.5+i*5, 52.5+j*5), 2)

    for e, char in enumerate(grid.rows[row]):
        if grid.is_accessible((e, row)) and (e, row) in grid.rolls:
            pygame.draw.circle(screen, GRID_COLOR, (52.5+e*5, 52.5+row*5), 2)
            grid.rows[e][row] = "."
            grid.rolls -= {(e, row)}
            rolls_removed = start_rolls - len(grid.rolls)

    row += 1
    if row == grid.height:
        row = 0

    num_rolls_text = str(rolls_removed)
    num_rolls_display = font.render(num_rolls_text, True, "white")
    num_rect = num_rolls_display.get_rect(center=(WIDTH / 2, 30))
    screen.blit(num_rolls_display, num_rect)

    pygame.display.flip()
    clock.tick(max(rolls_removed/50, 50))

pygame.quit()
