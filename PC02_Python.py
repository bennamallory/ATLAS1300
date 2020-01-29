# File name     : PC02_20190916_Benna_Mallory.py
# Version       : Python 3
# Purpose       : To practice basic drawing skills with turtles
# Author        : Mallory Benna 
# Date written  : 1-29-2020
# Description   : This program provides methods for creating an animation using turtles

#Import time and random modules
from turtle import *
from time import sleep
from random import randint

#Initialize variables
screen = Screen()

t1 = Turtle()
t1.pencolor("blue")
#t1.setBodyColor(blue)
t1.width(3)
t1.speed(10)

t2 = Turtle()
t2.pencolor("#34D2EB")
#t2.setBodyColor(makeColor(52,210,235))
t2.width(3)
t2.speed(10)

t3 = Turtle()
t3.pencolor("#1F81D1")
#t3.setBodyColor(makeColor(31,129,209))
t3.width(3)
t3.speed(10)

t4 = Turtle()
t4.pencolor("#38C225")
#t4.setBodyColor(makeColor(56,194,37))
t4.width(1)
t4.speed(10)

t5 = Turtle()
t5.pencolor("black")
#t5.setBodyColor(black)
#t5.width(10)
#t5.setHeight(10)
t5.width(20)
t5.speed(10)

i = 0
j = 0
k = 0
h = 0

lower = 0
upper = 0
duration = 0.5
width2 = 640
height = 480
dropPicX = 470
dropPicY = 320
leftBorderSize = 10
rightBorderSize = 620

#Methods to place turtles at start

def startTurtles():
  t1.up()
  t2.up()
  t3.up()
  t4.up()
  t5.up()
  t1.goto(-115,95)
  t2.goto(113,100)
  t3.goto(0,-50)

#Method to generate a random X value
def randX(lower,upper):
  x = randint(lower,upper)
  return x

#Method to generate a random Y value
def randY(lower,upper):
  y = randint(lower,upper)
  return y

#Method to make a single square
def makeSquare(turtle):
  turtle.down()
  for x in range(0,4):
    turtle.forward(100)
    turtle.right(90)
  turtle.up()
  
#Method to make a small square
def makeSmallSquare(turtle):
  turtle.down()
  for x in range(0,4):
    turtle.forward(3)
    turtle.right(90)
  turtle.up()
  
#Method to make a series of large squares
def manySquares(turtle):
  for x in range(0,7):
    makeSquare(turtle)
    turtle.right(5)
  turtle.up()

#Method to make a single triangle
def makeTriangle(turtle):
  turtle.down()
  for x in range(0,3):
    turtle.forward(100)
    turtle.right(120)
    
#Method to make a series of triangles
def manyTriangles(turtle):
  turtle.down()
  for x in range(0,10):
    makeTriangle(turtle)
    turtle.right(36)
  turtle.up()

#Method to drop a picture in world
def dropPic(turtle):
  turtle.up()
  turtle.geto(dropPicX,dropPicY)
  #pic = makePicture(pickAFile())
  #drop(turtle,pic)

#Method to layer a series of squares on top of triangle series
def secondLayer(turtle):
  for i in range(0,6):
    turtle.left(90)
    sleep(0.15)
    manySquares(turtle)


#Make animation

#Drop M
#dropPic(t5)

#Start turtles in assigned locations
startTurtles()

#Draw three main star-like objects
#Star 1
#sleep(duration)
manyTriangles(t1)

#Star 2
#sleep(duration)
manyTriangles(t2)

#Star 3
#sleep(duration)
manyTriangles(t3)

#Create rotating second layer on all three stars
sleep(duration)
secondLayer(t1)
secondLayer(t2)
secondLayer(t3)

#Draw the sections of small random squares around three main objects ( World Dimensions = W-640 X H -480 )

#Loop filling in bottom square section
while i < 900:
  #Left side
  #Bottom square
  t4.goto(randX(leftBorderSize,150),randY(300,450))
  makeSmallSquare(t4)
  
  #Right Side
  #Bottom square
  t4.goto(randX(470,rightBorderSize), randY(300,450))
  makeSmallSquare(t4)
  
  #Increase while loop by 1 each round
  i += 1
  
#Loop filling in middle rectangle section
while k < 500:
  #Left Middle rectangle
  t4.goto(randX(leftBorderSize,55), randY(80,300))
  makeSmallSquare(t4)
  
  #Right Middle rectangle
  t4.goto(randX(565,rightBorderSize), randY(80,300))
  makeSmallSquare(t4)
  
  #Increase while loop by 1 each round
  k += 1

#Loop filling in top square section
while h < 300:
  #Top Left square
  t4.goto(randX(leftBorderSize,85), randY(10,80))
  makeSmallSquare(t4)
  
  #Top Right square
  t4.goto(randX(545,rightBorderSize), randY(10,80))
  makeSmallSquare(t4)
  
  #Increase while loop by 1 each round
  h += 1
  
  
#Wipe out entire screen with scribbles after waiting
sleep(1.5)
#Blackout screen --> Move turtle to random points while drawing lines between each point
while j < 5000:
  t5.down()
  t5.goto(randX(0,width2), randY(0,height))
  j += 1
