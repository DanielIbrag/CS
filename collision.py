#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Nov, 9th 2023
#This program asks for user input.csv then prints out top 3 collisions and reasons
import pandas as pd

csvFile = input("Enter the name of the csv file: ")

collisions = pd.read_csv(csvFile)

print("The top three contributing factors for the primary vehichle of collisions in the file are:")
print(collisions["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])



