#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Nov 5th, 2023
#This program asks for a csv file and an attribute and prints the attribute and the top 10 values of the attribute
import pandas as pd
csvFile = input("Enter the name of the csv file: ")
att = (input("Enter the attribute: "))
tickets = pd.read_csv(csvFile)
print("The 10 worst offenders are:")
print(tickets[att].value_counts()[:10])