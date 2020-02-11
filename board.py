import pygame

def build_game_board(width, height):
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.init()
    pygame.display.set_caption("Chess")
    pygame.display.get_surface().fill((255,255,255))
    pygame.display.update()
    isWhite = True

    for y in range(8):
        for x in range(8):
            color = [255,255,255] if isWhite else [0,0,0]
            pygame.draw.rect(screen, color, pygame.Rect(x * int(width/8), y * int(height/8), int(width/8), int(height/8)))
            isWhite = not isWhite
        isWhite = not isWhite

    pygame.display.update()

build_game_board(600, 600)

blnExitGame = False
while not blnExitGame:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        blnExitGame = True
    elif event.type == pygame.VIDEORESIZE:
        width, height = pygame.display.get_window_size()
        build_game_board(width, height)
