#find the average and maximum population of a borough
import pandas as pd
import matplotlib.pyplot as plt 
borough = input("Enter borough name: ")
pop = pd.read_csv('nycHistPop.csv',skiprows=5)
pop['Fraction'] = pop[borough]/pop['Total']

print("The average population of", borough, "is", pop['Fraction'].mean())
print("The maximum population of", borough, "is", pop['Fraction'].max())
