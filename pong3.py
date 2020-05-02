import pygame

pygame.init()

WIDTH = 300
HEIGHT = 200
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

SCREEN.fill(RED)
pygame.display.flip()

radius = 25
x = WIDTH//2
y = HEIGHT//2
pygame.draw.circle(SCREEN, WHITE, (x, y), radius)  # Position is the center of the circle.


end = False
while not end:
    SCREEN.fill(RED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    key = pygame.key.get_pressed()

    if key[pygame.K_a]:
        x = radius
        y = radius

    if key[pygame.K_z]:
        x = WIDTH - radius
        y = radius

    if key[pygame.K_q]:
        x = radius
        y = HEIGHT - radius

    if key[pygame.K_s]:
        x = WIDTH - radius
        y = HEIGHT - radius

    pygame.draw.circle(SCREEN, WHITE, (x, y), radius)

    pygame.display.update()

pygame.quit()