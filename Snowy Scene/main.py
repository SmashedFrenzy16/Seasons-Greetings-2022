import pygame
import random

pygame.init()

screen = pygame.display.set_mode((785, 350))

pygame.display.set_caption("Snowy Scene")

# Background picture from freepik.com

background = pygame.image.load("snow-scene.jpeg")

snowflake_img = []
snowflake_x = []
snowflake_y = []
snowflake_y_change = []
snowflake_num = 20

text_font = pygame.font.Font("freesansbold.ttf", 50)

for i in range(snowflake_num):

    # <a href="https://www.flaticon.com/free-icons/autumn" title="autumn icons">Autumn icons created by iconixar - Flaticon</a>

    snowflake_img.append(pygame.image.load("snowflake.png"))
    snowflake_x.append(random.randint(0, 785))
    snowflake_y.append(random.randint(0, 350))
    snowflake_y_change.append(0.6)

def flakes(x, y, i):

    screen.blit(snowflake_img[i], (x, y))

running = True

while running:

    screen.fill((255, 255, 255))

    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    # Leaf movement

    for i in range(snowflake_num):


        snowflake_y[i] += snowflake_y_change[i]

        if snowflake_y[i] >= 600:

            snowflake_x[i] = random.randint(0, 785)
            snowflake_y[i] = random.randint(0, 350)

        flakes(snowflake_x[i], snowflake_y[i], i)

    pygame.display.update()