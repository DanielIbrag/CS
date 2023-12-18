#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Sep 25th 2023
#This program asks for user input then purps it out

import matplotlib.pyplot as plt
import numpy as np
inp = input("Enter name of the input file:  ")
out = input("Enter name of the input file:  ")
img = plt.imread(inp)
plt.imshow(img)
plt.show()

img2 = img.copy()
img2[:,:,1] = 0 

plt.imshow(img2)
plt.show()

plt.imsave(out, img2)