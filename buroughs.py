#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Oct 9th 2023
#This program asks for user input for a burough then saves it as a png file
import matplotlib.pyplot as plt
import pandas as pd 

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
borough = (input("Enter borough name: "))
output = (input("Enter output file name: "))
pop['Fraction'] = pop[borough]/pop['Total']
pop.plot(x='Year', y = 'Fraction')
plt.savefig(output)
# plt.show()


