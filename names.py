#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Oct 23rd 2023
#This program sorts a list of names then prints that list out in alphabetical order by last name

names = input("Enter names: ")
names = names.split("; ")
for i in range(len(names)):
    names[i] = names[i].split(", ")

names.sort()
    
for i in range(len(names)):
    names[i] = names[i][1] + " " + names[i][0]
    print(names[i])
    