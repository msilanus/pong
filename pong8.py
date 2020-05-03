import pygame
from random import randint, random

pygame.init()

WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Pong Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

wallSound = pygame.mixer.Sound("sounds/wall.wav")
pingSound = pygame.mixer.Sound("sounds/ping2.wav")
goalSound = pygame.mixer.Sound("sounds/goal.wav")

ball = {}
paddle = {}
score = 0
best_score = 0
speed = 5
x_sens = y_sens = 1
pause = False
quit = False
end = False

myfont = pygame.font.SysFont('monospace', 50)

def start_game():
    for second in range(4):
        SCREEN.fill(BLACK)
        start = myfont.render("Game starts in :", False, GREEN)
        SCREEN.blit(start, (WIDTH // 2 - start.get_width() // 2, HEIGHT // 2 - start.get_height() * 2))
        start = myfont.render(str(3 - second), False, GREEN)
        SCREEN.blit(start, (WIDTH // 2 - start.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(1000)

def init():
    ball["radius"] = 10
    ball["x"] = WIDTH//2
    ball["y"] = 10
    pygame.draw.circle(SCREEN, WHITE, (ball["x"], ball["y"]), ball["radius"])  # Position is the center of the circle.

    paddle["width"] = 200
    paddle["height"]= 20
    paddle["color"] = BLUE
    paddle["x"] = WIDTH//2 - paddle["width"]//2
    paddle["y"] = HEIGHT - paddle["height"]
    pygame.draw.rect(SCREEN, paddle["color"],(paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

    global score
    score = 0
    global speed
    score = 0
    global speed
    speed = 5
    global x_sens
    global y_sens
    x_sens = y_sens = 1
    global pause
    global quit
    global end
    pause = quit = end = False

start_game()
init()
while not quit:
    clock = pygame.time.Clock()
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


        if not pause:

            if key[pygame.K_LEFT]:
                #print("Key LEFT pressed")
                paddle["x"] = paddle["x"] - speed
                if paddle["x"] < 0:
                    paddle["x"] = 0

            if key[pygame.K_RIGHT]:
                #print("Key RIGHT pressed")
                paddle["x"] = paddle["x"] + speed
                if paddle["x"] > WIDTH - paddle["width"]:
                    paddle["x"] = WIDTH - paddle["width"]

            if ball["x"]<ball["radius"] or ball["x"] > WIDTH-ball["radius"]:
                x_sens = -x_sens
                #wallSound.play()

            if ball["y"]<ball["radius"]:
                y_sens = -y_sens
                #wallSound.play()

            if ball["y"]+ball["radius"]>paddle["y"]:
                if ball["x"]<paddle["x"]+paddle["width"] and ball["x"]>paddle["x"]:
                    pingSound.play()
                    y_sens = -y_sens
                    score += 1
                    if score % 5 == 0:
                        speed+=1
                        print(f"Speed : {speed}")

                    if score % 10 == 0:
                        paddle["width"] -= 20
                        speed -= 1


            if ball["y"] > HEIGHT-ball["radius"]:
                goalSound.play()
                end = True
                gameover = myfont.render("GAME OVER !".format(score), False, RED)
                SCREEN.blit(gameover, (WIDTH//2 - gameover.get_width()//2, HEIGHT//2 - gameover.get_height()//2))
                display_score = myfont.render("Your Score : {0}".format(score), False, RED)
                SCREEN.blit(display_score, (WIDTH//2 - display_score.get_width()//2, 2*HEIGHT//3))
                pygame.display.update()
                pygame.time.delay(2000)

            ball["x"] = ball["x"] + x_sens * speed
            ball["y"] = ball["y"] + y_sens * speed


        pygame.draw.circle(SCREEN, WHITE, (ball["x"], ball["y"]), ball["radius"])
        pygame.draw.rect(SCREEN, paddle["color"], (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

        display_score = myfont.render("Score : {0}".format(score), False, GREEN)
        SCREEN.blit(display_score, (10, 0))

        if score > best_score:
            best_score = score
        display_best_score = myfont.render("Best : {0}".format(best_score), False, GREEN)
        SCREEN.blit(display_best_score, (WIDTH - display_best_score.get_width() - 2 , 0))
        pygame.display.update()
        #pygame.time.delay(10)
        clock.tick(100)

    SCREEN.fill(BLACK)
    pygame.display.update()
    pygame.time.delay(200)
    restart = myfont.render("INSERT COIN TO PLAY (R)", False, GREEN)
    SCREEN.blit(restart, (WIDTH//2 - restart.get_width()//2, HEIGHT//2 - restart.get_height()//2))
    pygame.display.update()
    pygame.time.delay(200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
            quit = True

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        quit = True

    if key[pygame.K_r]:
        init()
        start_game()

pygame.quit()