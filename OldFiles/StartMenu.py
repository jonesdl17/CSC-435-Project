import pygame
import os

blitzMode = False
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
txtQuestion = questionFont.render("What game mode?", True, white)
txtNormal = font.render("Normal", True, white)
txtBlitz = font.render("Blitz", True, white)
txtStart = font.render("Start", True, white)


screen.fill(black)
running = True
while running:
    #if the game is xed out the program stops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Drawing red rectangles under start/blitz/normal
    pygame.draw.rect(screen, red, ( 325, 345,100,30))
    pygame.draw.rect(screen, red, (90, 345, 100,30))
    pygame.draw.rect(screen, red, ( 200, 395, 100, 30))
    
    #Getting coordiantes of mouse to change colors
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #Blitz button color change
    if 190 >= mouse[0] >= 90 and 375 >= mouse[1] >= 345:
        pygame.draw.rect(screen, blue, (90, 345, 100,30))
        if click[0] == 1:
            blitzMode = True
    #Normal button color change 
    if 425 >= mouse[0] >= 325 and 375 >= mouse[1] >= 345:
        pygame.draw.rect(screen, blue, ( 325, 345,100,30))
        if click[0] == 1:
            blitzMode = False
    #start button color change 
    if 325 >= mouse[0] >= 225 and 430>= mouse[1] >= 395:
        pygame.draw.rect(screen, red, ( 200, 395, 100, 30))
        if click[0] == 1:
            pygame.display.quit()
            running = False
            os.system("board.py")
            
    
    screen.blit(txtQuestion, (160, 160))
    screen.blit(txtNormal, (100,350))
    screen.blit(txtBlitz, (350, 350))
    screen.blit(txtStart, (225, 400))
    
    pygame.display.update()
print(blitzMode)
    

