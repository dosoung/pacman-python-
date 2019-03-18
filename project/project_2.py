import pygame
from pygame.locals import *
import numpy from loadtxt
import Tile FROM tiles




pygame.init()
screen = pygame.display.set_mode((320,320), 0, 32)
width, height = (32, 32)
tiles = []
layout = loadtxt('tilemap_test.txt', dtype=str)
rows, cols = layout.shape
for col in range(cols):
    for row in range(rows):
        value = layout[row][col]
        if value != '0':
            pos = (col*width, row*height)
            tiles.append(Tile((width, height), pos))

background = pygame.surface.Surface((320,320)).convert()
background.fill((0,0,0))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0,0))
    for tile in tiles:
        tile.draw(screen)
    pygame.display.update()
