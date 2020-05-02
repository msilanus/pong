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

speed = 1
x_sens = y_sens = 1
auto = True


end = False
while not end:
    SCREEN.fill(RED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    key = pygame.key.get_pressed()

    if key[pygame.K_o]:
        auto = True

    if key[pygame.K_m]:
        auto = False

    if not auto:

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

        if key[pygame.K_UP]:
            print("Key UP pressed")
            y = y - speed
            if y<radius:
                y = radius

        if key[pygame.K_DOWN]:
            print("Key DOWN pressed")
            y = y + speed
            if y > HEIGHT -radius:
                y =  HEIGHT -radius

        if key[pygame.K_LEFT]:
            print("Key LEFT pressed")
            x = x - speed
            if x < radius:
                x = radius

        if key[pygame.K_RIGHT]:
            print("Key RIGHT pressed")
            x = x + speed
            if x > WIDTH - radius:
                x = WIDTH - radius

    else:
        if x<radius or x > WIDTH-radius:
            x_sens = -x_sens

        if y<radius or y > HEIGHT-radius:
            y_sens = -y_sens

        x = x + x_sens * speed
        y = y + y_sens * speed


    pygame.draw.circle(SCREEN, WHITE, (x, y), radius)

    pygame.display.update()
    pygame.time.delay(10)

pygame.quit()