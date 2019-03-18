import pygame
import pygame as pg # pygame 모듈을 pg로 선언 가능
import threading
import random
pygame.init() #pygame 모듈 초기화

#전역변수 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 187, 0)

 # 게임 창 크기 설정
sizewidth = 640
sizeheight = 640
screen = pygame.display.set_mode((sizewidth,sizeheight),0,32) # GUI창을 설정
pygame.display.set_caption("PACMAN") #게임 타이틀 창에 제목부분
screen.fill(BLACK)

#맵설정
width, height = (32, 32)
map_data = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
           [1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
           [1,1,1,1,0,1,1,1,0,1,0,0,1,1,1,0,1,1,1,1],
           [0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0],
           [1,1,1,1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,1,1],
           [0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0],
           [1,1,1,1,0,1,0,1,0,0,0,1,0,0,1,0,1,1,1,1],
           [0,0,0,1,0,1,0,1,1,1,1,1,0,0,1,0,1,0,0,0],
           [1,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1],
           [1,0,0,0,0,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1],
           [1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,1],
           [1,0,0,1,0,1,1,1,0,1,0,0,1,1,1,0,1,0,0,1],
           [1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1],
           [1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
           [1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1,0,1],
           [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]



for i in range(20):
    for j in range(20):
        tiles = map_data[j][i]
        if tiles == 1:
            pygame.draw.rect(screen,BLUE,[i*32,j*32,width,height])
        elif tiles == 0:
            pygame.draw.rect(screen,ORANGE,[i*32+16,j*32+16,5,5])


#팩맨이미지 설정
pacman = pygame.image.load('image_1.jpg')
pacman = pygame.transform.scale(pacman,(32,32))
pacmanX, pacmanY =(9,10)
rotated = pygame.transform.rotate(pacman,0)

#팩맨 이동시 이미지 지우기
backup = pygame.image.load('image_2.png')
backup = pygame.transform.scale(backup,(32,32))

moveLEFT = False
moveRIGHT = False
moveUP = False
moveDOWN = False

#고스트 설정
ghost_1 = pygame.image.load('ghost_1.png')
ghost_1 = pygame.transform.scale(ghost_1,(32,32))
ghost_1X, ghost_1Y = (9,7)






#이동시간 설정



done = False
clock = pygame.time.Clock() #유저가 클로즈 버튼 누르기전까지 지속됌 루프가 게임의 FPS 를 설정 할 수 있다.

while not done:
    clock.tick(6) #초당 화면에  n번의 화면을 출력하겠다  많이 출력할 수록 cpu 많이 잡아먹 or 출력 높으면 모니터가 제대로 출력 못하는 경우도 발생

     #MAIN EVENT LOOP
    for event in pygame.event.get(): # 게임중간에 발생한 이벤트를 캐치하여 검사 (마우스클릭,키보드 클릭등 인지 하고 어떤 이벤트인지 검
        if event.type ==pygame.QUIT:
                done = True

        #키보드입력 시켜 팩맨이동
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLEFT = True
            elif event.key == pygame.K_RIGHT:
                moveRIGHT = True
            elif event.key == pygame.K_UP:
                moveUP = True
            elif event.key ==pygame.K_DOWN:
                moveDOWN = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLEFT = False
            elif event.key == pygame.K_RIGHT:
                moveRIGHT = False
            elif event.key == pygame.K_UP:
                moveUP = False
            elif event.key == pygame.K_DOWN:
                moveDOWN = False



 # 고스트 이동
    while(ghost_1X or ghost_1Y == 0):
        backup_ghost_1X = ghost_1X
        backup_ghost_1Y = ghost_1Y

        ghost_place = random.choice([ghost_1X-1,ghost_1X+1,ghost_1Y-1,ghost_1Y+1])

        if ghost_place == (ghost_1X-1) or (ghost_1X+1):
            ghost_1X = ghost_place
        elif ghost_place == (ghost_1Y-1) or (ghost_1Y+1):
            ghost_1Y = ghost_place

        if ghost_1X ==1:
            ghost_1X = backup_ghost_1X
        elif ghost_1Y ==1:
            ghost_1Y = backup_ghost_1Y    

        screen.blit(ghost_1,(ghost_1X*32,ghost_1Y*32))


    backupX = pacmanX
    backupY = pacmanY

#팩맨이동
    if moveLEFT == True:
        pacmanX -=1
        rotated = pygame.transform.rotate(pacman,180)
    elif moveRIGHT == True:
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

    if pacmanX < 0 :
        pacmanX = 19
    elif pacmanX >19:
        pacmanX = 0

    screen.blit(backup,(backupX*32,backupY*32))
    screen.blit(rotated,(pacmanX*32,pacmanY*32))
    pygame.display.flip()

pygame.quit(1)
