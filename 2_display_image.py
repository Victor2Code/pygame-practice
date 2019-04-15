#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3

import pygame

pygame.init()

display_width=800
display_height=600
car_width=73

black=(0,0,0)
white=(255,255,255)

gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')
clock=pygame.time.Clock()

carImage=pygame.image.load('racecar_1.png')
def car(x,y):
    gameDisplay.blit(carImage,(x,y))


def game_loop():
    x=display_width*0.45
    y=display_height*0.8
    x_changed=0
    
    exitGame=False

    while not exitGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame=True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_changed=-5
                elif event.key==pygame.K_RIGHT:
                    x_changed=5
            if event.type==pygame.KEYUP:
                x_changed=0
            #print(event)
        x+=x_changed
        gameDisplay.fill(white)
        car(x,y)
        if x>display_width-car_width or x<0:
            exitGame=True 
        pygame.display.update()
        clock.tick(30)

game_loop()
pygame.quit()
quit()
