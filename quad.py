# Write a program that asks the user for the name of an image, the name of an output file. Your program should then save the lower left quarter of the image to the output file specified by the user using only one loop.


import matplotlib.pyplot as plt
import numpy as np

img = plt.imread(input("Enter the name of the image: "))
out = input("Enter the name of the output file: ")

for i in range(len(img)):
    for j in range(len(img[i])):
        if i > len(img)/2 and j < len(img[i])/2:
            img[i][j] = [1, 0, 0]

plt.imsave(out, img)
