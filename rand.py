#Name: Daniel Ibragimov
#Date: Nov 12th, 2023
#get a random number between 1-100 and print it
import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(10)
  a = random.randrange(0,359)
  trey.right(a)