#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: september 18th, 2023
#This program prints a reversed string 2 times

message = input("enter a message: ")
reverse = message[::-1]
for i in reverse:
    print(i + " " + i)