#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3

import pygame

pygame.init()

display_width=800
display_height=600

black=(0,0,0)
white=(255,255,255)

gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')
clock=pygame.time.Clock()

carImage=pygame.image.load('racecar_1.png')
def car(x,y):
    gameDisplay.blit(carImage,(x,y))

crashed=False

x=display_width*0.45
y=display_height*0.8

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed=True
        #print(event)

    gameDisplay.fill(white)
    car(x,y)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
