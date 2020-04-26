def count_down():
    global turn, color
    white = False
    black = True
    if(color == 1):
        white = True
        black = False
    whiteTime = 300
    blackTime = 300
    wM,wS = divmod(whiteTime, 60)
    bM,bS = divmod(blackTime, 60 )
    
    font = pygame.font.Font('freesansbold.ttf', 20) 
    
    while whiteTime >0 and blackTime >0:
        if(turn and white):
            whiteTime -=1
            time.sleep(1)
        elif(turn and black):
            blackTime -=1
            time.sleep(1)
        elif(not turn and white):
            blackTime -=1
            time.sleep(1)
        else:
            whiteTime -=1
            time.sleep(1)
        wM,wS = divmod(whiteTime, 60)
        bM,bS = divmod(blackTime, 60)
        whiteText = font.render("White Time: " +str(wM) +":"+str(wS), True, (0,0,0))
        blackText = font.render("Black Time: " +str(bM) +":"+str(bS), True, (0,0,0))
        screen.blit(whiteText, (130,40))
        screen.blit(blackText, (320,40))
        pygame.display.update()
         