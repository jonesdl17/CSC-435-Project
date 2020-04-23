import pygame
from board import init_game


#Declaring variables
#declaring dimensions and colors
width, height = 600, 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (94,25,20)
blue =(13, 213, 252)
#creating screen
pygame.init()
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("Chess")
#Creating texts
questionFont = pygame.font.Font(None, 42)
font = pygame.font.Font(None, 32)
txtQuestion = questionFont.render("Are you ready?", True, white)
txtStart = font.render("Start", True, white)
txtQuit = font.render("Quit", True, white)
#Creating buttons
btnStart = pygame.draw.rect(screen,(100,100,50), (100,350,100,100))
btnQuit  = pygame.draw.rect(screen,(100,100,50), (350,350,100,100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    pygame.draw.rect(screen, red, ( 325, 345,100,30))

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 190 >= mouse[0] >= 90 and 375 >= mouse[1] >= 345:
        pygame.draw.rect(screen, blue, (90, 345, 100,30))
        if click[0] == 1:
            init_game(1)
            running = False
    else:
        pygame.draw.rect(screen, red, (90, 345, 100,30))
    if 425 >= mouse[0] >= 325 and 375 >= mouse[1] >= 345:
        pygame.draw.rect(screen, blue, ( 325, 345,100,30))
        if click[0] == 1:
            running = False
    else:
        pygame.draw.rect(screen, red, ( 325, 345,100,30))


    screen.blit(txtQuestion, (160, 160))
    screen.blit(txtStart, (100,350))
    screen.blit(txtQuit, (350, 350))
    
    pygame.display.update()