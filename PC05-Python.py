# File name     : PC05_20191009_Benna_Mallory.py
# Version       : Python 3
# Purpose       : To practice using the gui module for animations
# Author        : Mallory Benna 
# Partner       : Catherine Jones
# Date written  : 10-03-2019
# Date revised  : 1-29-2020
# Description   : This is a program used to create a petri dish of animated microbes
#     Revisions   10-04-2019 -- fixed microbe function to be generalized for various types of microbes
#                               added movement functions
#                 1-29-20 -- Converted to python


#Modules
from pygame.draw import *
import pygame
from time import sleep
from random import randint

#Variables
#----------------
# Microbe function variables
circle = "circle"
oval = "oval"
rectangle = "rectangle"
polygon = "polygon"

# Animation variables 
global x
global y
x = randint(80,370)
y = randint(80,370)
shapes = [circle,rectangle,polygon,oval]
microbeList = []

#Define colors
BLACK = [0,0,0]
WHITE = [255,255,255]
RED = [255,0,0]
BLUE = [0,0,255]
GREEN = [0,255,0]

colorsList = [BLACK,WHITE,RED,BLUE,GREEN]


#Creating Display with Circular Petri Dish
#-------------------------
pygame.init()
size = [500,500]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Petri Dish")

screen.fill(BLACK)
petri = pygame.draw.circle(screen,WHITE,[250,250],240)


#Method to create microbes that vary in size, color, starting position, and shape
#-------------------------

def makeMicrobe(x,y,color=BLACK,shape=circle):
  #Create initial microbe objects of specified size
  circleMicrobe = pygame.draw.circle(screen,color,[randint(70,415),randint(75,415)],12)
  #ovalMicrobe = pygame.draw.ellipse(screen,color,[100,75,95,100],0)
  #rectMicrobe = pygame.draw.rect(screen,color,[100,115,125,100])
  polyMicrobe = pygame.draw.polygon(screen,color,[[260,225],[225,250],[185,225],[175,250]])

  
  #Set initial microbes to specific x,y position
  if shape == circle:
    circleMicrobe.move(x,y)
    pygame.display.update()
    return circleMicrobe
  elif shape == oval:
    #ovalMicrobe.move(x,y)
    pygame.display.update()
    #return ovalMicrobe
  elif shape == rectangle:
    #rectMicrobe.move(x,y)
    pygame.display.update()
    #return rectMicrobe
  elif shape == polygon:
    polyMicrobe.move(x,y)
    pygame.display.update()
    return polyMicrobe


#Methods to Move Microbes
#-------------------------
done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True;
    
    #Erase screen
    screen.fill(BLACK)
    petri = pygame.draw.circle(screen,WHITE,[250,250],240)
    
    # Draw updated picture
    for microbe in range(4):
        microbeList.append(makeMicrobe(randint(40,360),randint(40,360),[randint(0,255),randint(0,255),randint(0,255)],shapes[randint(0,3)]))
