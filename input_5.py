#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Sep 26th, 2023
#This program asks user for 5 numbers then moves turtle by that number

import turtle
var = [1,2,3,4,5]
tim = turtle.Turtle()

for i in range(5):
    var[i] = input("please enter a number: ")
    tim.left(int(var[i]))
    tim.forward(100)