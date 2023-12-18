#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: september 25th, 2023
#This program asks for a hex string, then prints out a turtle with that string
import turtle

colorio = input("Enter a hex string: ")
buddy = turtle.Turtle()
buddy.color(colorio)
buddy.shape("turtle")
buddy.stamp()