import pygame

import sys

import os

from pygame.locals import *

def drawGrid():
    midx = int(WINDOW_WIDTH/2)
    midy = int(WINDOW_HEIGHT/2)
    startx = midx-200
    stopx = midx+200
    starty = midy-300
    stopy = midy+300

    #drawing the grid
    for x in range(startx, stopx, blockSize):
        for y in range(starty, stopy, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            Grid.append(rect)
            pygame.draw.rect(screen, WHITE, rect, 1)

def check_pressed ():
    centre_x = blockSize/2
    centre_y = blockSize/2
    mousex ,mousey = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #loop to check which cell was pressed
    for cell in Grid:
        if mousex > cell.x and mousex < cell.x + blockSize and mousey > cell.y and mousey < cell.y + blockSize:
            # pygame.mouse.set_visible(0)
            pygame.draw.circle(screen, (140,0,100), (centre_x+cell.x, centre_y+cell.y), 20)


global WHITE,WINDOW_HEIGHT,WINDOW_WIDTH,Grid,blockSize,screen
blockSize = 60
Grid = []
WHITE = (200,200,200)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

pygame.init()  # initialize pygame

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250,250,250))
screen.blit(background, (0,0))

pygame.mouse.set_visible(1)

pygame.display.set_caption('Chain Reaction Game')

while True:
    clock.tick(60)# Max FPS
    # screen.blit(bg, (0, 0))
    x, y = pygame.mouse.get_pos()
    drawGrid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            check_pressed()

    pygame.display.update()#Refreshes the screen

