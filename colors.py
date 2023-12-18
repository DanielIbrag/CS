#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Sep 15th, 2023
#This program shows all shades of blue in a teardrop

import turtle				

turtle.colormode(255)		
tess = turtle.Turtle()		
tess.shape("turtle")		
tess.backward(100)			


for i in range(0,255,10):
     tess.forward(10)		
     tess.pensize(i)		
     tess.color(0,0,i)		