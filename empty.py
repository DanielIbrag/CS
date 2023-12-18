#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Nov 13th 2023
#This program asks for user input if the string is empty it asks again
mess = ""
while mess == "":
    mess = input("Enter a non-empty string:")
    if mess == "":
        print("That was empty.  Try again.")
    else:
            print("You entered:", mess)
        