#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Oct 23rd 2023
#This program prints a boro fraction

import matplotlib.pyplot as plt
import pandas as pd


pop = pd.read_csv('nycHistPop.csv',skiprows=5)
borough = input("Enter borough name: ")
print("The average population of", borough, "is", pop[borough].mean())
print("The maximum population of", borough, "is", pop[borough].max())

