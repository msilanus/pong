import pygame
from random import randint, random

pygame.init()

WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

SCREEN.fill(BLACK)
pygame.display.flip()

radius = 10
x = WIDTH//2
y = radius

pygame.draw.circle(SCREEN, WHITE, (x, y), radius)  # Position is the center of the circle.


paddle = { "width" : 200,
           "height": 20,
           "color" : BLUE,
           "x"     : 0,
           "y"     : HEIGHT}
paddle["x"] = WIDTH//2 - paddle["width"]//2
paddle["y"] = HEIGHT - paddle["height"]
pygame.draw.rect(SCREEN, paddle["color"],(paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

speed = 5
x_sens = y_sens = 1
pause = False


end = False
while not end:
    SCREEN.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        pause = True

    if key[pygame.K_RETURN]:
        pause = False

    if key[pygame.K_m]:
        auto = False

    if not pause:

        if key[pygame.K_LEFT]:
            print("Key LEFT pressed")
            paddle["x"] = paddle["x"] - speed
            if paddle["x"] < 0:
                paddle["x"] = 0

        if key[pygame.K_RIGHT]:
            print("Key RIGHT pressed")
            paddle["x"] = paddle["x"] + speed
            if paddle["x"] > WIDTH - paddle["width"]:
                paddle["x"] = WIDTH - paddle["width"]

        if x<radius or x > WIDTH-radius:
            x_sens = -x_sens

        if y<radius:
            y_sens = -y_sens

        if y+radius>paddle["y"]:
            if x<paddle["x"]+paddle["width"] and x>paddle["x"]:
                y_sens = -y_sens

        if y > HEIGHT-radius:
            end = True

        x = x + x_sens * speed
        y = y + y_sens * speed


    pygame.draw.circle(SCREEN, WHITE, (x, y), radius)
    pygame.draw.rect(SCREEN, paddle["color"], (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

    pygame.display.update()
    pygame.time.delay(10)

pygame.quit()