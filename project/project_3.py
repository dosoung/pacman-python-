




moveLEFT = False
moveRIGHT = False
moveUP = False
moveDOWN = False


while not done:
    clock.tick(90)

    for event in pygame.event.get():
        backupX = pacmanX
        backupY = pacmanY

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLEFT = True
            elif event.key == pygame.K_RIGHT:
                moveRIGHT = True
            elif event.key == pygame.K_UP:
                moveUP = True
            elif event.key ==pygame.K_DOWN:
                moveDOWN = True

        if event.type == pygame.kEYUP:
            if event.key == pygame.K_LEFT:
                moveLEFT = False
            elif event.key == pygame.K_RIGHT:
                moveRIGHT = False
            elif event.key == pygame.K_UP:
                moveUP = False
            elif event.key == pygame.K_DOWN:
                moveDOWN = False

        if moveLEFT == True:
            pacmanX -=1
            rotated = pygame.transform.rotate(pacman,180)
        elif moveRIGHT ==True:
            pacmanX +=1
            rotated = pygame.transform.rotate(pacman,0)
        elif moveUP == True:
            pacmanY -=1
            rotated = pygame.transform.rotate(pacman,90)
        elif moveDOWN == True:
            pacmanY +=1
            rotated = pygame.transform.rotate(pacman,-90)

        if map_data[pacmanY][pacmanX] == 1:
            pacmanX = backupX
            pacmanY = backupY

        if pacmanX < 0 or pacmanX > 19 :
            pacmanX = backupX

        screen.blit(backup,(backupX*32,backupY*32))
        screen.blit(rotated,(pacmanX*32,pacmanY*32))
        pygame.display.update()

    if event.type ==pygame.QUIT:
            done = True

pygame.quit(1)
