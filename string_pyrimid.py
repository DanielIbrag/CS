#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Sep 27th, 2023
#This program makes a pyrimid string
s = input("Enter a striing: ")
ls = len(s)
for i in range(0,ls+1):
    print(s[:i])
for i in range(0,ls+1):
    print(s[i:])

print("Thank you for using my program!")