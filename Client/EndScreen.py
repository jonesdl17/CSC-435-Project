import pygame
import os
import sys


class EndScreen():
    running = True
    def __init__(self):
        Ruinning = True
        
    def displayScreen(self, turn, capturedKingColor):
        playerColor = -1
        capturedKingColor = -1
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
        Font = pygame.font.Font(None, 42)
        font = pygame.font.Font(None, 32)
        txtWin = Font.render("Congratulations!", True, white)
        txtWin2 = Font.render("You Have Won!", True, white)
        txtLost = Font.render("Defeat!", True, white)
        txtLost2 = Font.render("Better Luck Next Time!", True, white)
        txtQuit = font.render("Quit", True, white)

        screen.fill(black)
        running = True
        while running:
        #if the game is xed out the program stops
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exit()

            if(turn != True):
                screen.blit(txtLost, (180, 150))
                screen.blit(txtLost2, (160, 250))
            else:
                screen.blit(txtWin, (160,160))
                screen.blit(txtWin2, (160,250))
            pygame.draw.rect(screen, red, ( 325, 345,100,30))

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 425 >= mouse[0] >= 325 and 375 >= mouse[1] >= 345:
                pygame.draw.rect(screen, blue, ( 325, 345,100,30))
                if click[0] == 1:
                    running = False
                    sys.exit()
            else:
                pygame.draw.rect(screen, red, ( 325, 345,100,30))
            screen.blit(txtQuit, (350, 350))

    
            pygame.display.update()
    



