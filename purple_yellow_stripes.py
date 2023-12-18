#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Oct 3rd, 2023
#This program makes a png file with purple and yellow stripes
import numpy as np
import matplotlib.pyplot as plt
size = int(input("Enter the size of the image: "))
name = input("Enter the name of the output file: ")
img = np.zeros((size,size,3))

for i in range(size):
    if i%2 == 0:
        img[i] = [1,0,1]
    else:
        img[i] = [1,1,0]



plt.imsave(name,img)
# plt.imshow(img)
# plt.show()




