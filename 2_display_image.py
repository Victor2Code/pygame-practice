#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3

import pygame
import time 
import random
import pysnooper

pygame.init()

display_width=800
display_height=600
car_width=73
car_height=82

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')
clock=pygame.time.Clock()

carImage=pygame.image.load('racecar_1.png')
def dodged(count):
    dodgeFont=pygame.font.SysFont(None,25)
    dodgeText=dodgeFont.render('Dodged:'+str(count),True,red)
    gameDisplay.blit(dodgeText,(0,0))


def car(x,y):
    gameDisplay.blit(carImage,(x,y))

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def text_object(text,font_name,font_size,font_color):
    largeText=pygame.font.Font(font_name,font_size)
    textSurface=largeText.render(text,True,font_color)
    return textSurface,textSurface.get_rect()

def message_display(text,font_name,font_size,font_color):
    textSurf,testRect=text_object(text,font_name,font_size,font_color)
    testRect.center=(display_width/2,display_height/2)
    gameDisplay.blit(textSurf,testRect)
    pygame.display.update()
    #blit and update to add new object to display surface
    time.sleep(2)

def crash():
    message_display('You Crashed','freesansbold.ttf',100,red)
@pysnooper.snoop('/home/fuhx/github/pygame-practice/test.log')
def game_loop():
    x=display_width*0.45
    y=display_height*0.8
    x_changed=0
    
    thing_startx=random.randrange(0,display_width)
    thing_starty=-600
    thing_speed=7
    thing_width=100
    thing_height=100
    
    dodged_num=0 

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
        
        things(thing_startx,thing_starty,thing_width,thing_height,black)
        car(x,y)
        dodged(dodged_num)
        
        thing_starty+=thing_speed
        if thing_starty>display_height:
            thing_startx=random.randrange(0,display_width)
            thing_starty=0-thing_height
            dodged_num+=1
            thing_speed+=0.5
        
        #crash handling
        if y<thing_starty+thing_height and y>thing_starty-car_height and x>thing_startx-car_width and x<thing_startx+thing_width:
            crash()
            x=display_width*0.45
            y=display_height*0.8
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,display_width)
            dodged_num=0
            thing_speed=7
            car(x,y)
        #car(x,y)
        if x>display_width-car_width or x<0:
            crash()
            x=display_width*0.45
            y=display_height*0.8
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,display_width)
            dodged_num=0
            thing_speed=7
            car(x,y)
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
