#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Sep 25th 2023
#This program asks for user input then counts the white pixels
import matplotlib.pyplot as plt
import numpy as np

image  = input("Enter the name of the image file: ")
ca = plt.imread(image)
countSnow = 0
t = 0.75

for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
               countSnow = countSnow + 1

print("Snow count is", countSnow)
