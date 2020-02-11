import pygame

screen= pygame.display.set_mode([800, 800])

pygame.display.init()

isWhite = True

for y in range(8):
    for x in range(8):
        color = [255,255,255] if isWhite else [0,0,0]
        pygame.draw.rect(screen, color, pygame.Rect(x * 100, y * 100,100,100))
        isWhite = not isWhite
    isWhite = not isWhite

pygame.display.update()

blnExitGame = False
while not blnExitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            blnExitGame = True
