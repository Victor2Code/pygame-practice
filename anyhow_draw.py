#!usr/bin/env python
#python 3

import pygame

pygame.init()
gameDisplay=pygame.display.set_mode((300,300))
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameDisplay.fill(white)
    pixelArr=pygame.PixelArray(gameDisplay)

    for i in range(20,100):
        pixelArr[i][20]=red

    pygame.draw.line(gameDisplay,blue,(30,30),(40,40))
    pygame.draw.circle(gameDisplay,black,(50,50),10)
    pygame.draw.rect(gameDisplay,red,[100,100,20,20])
    pygame.display.update()




