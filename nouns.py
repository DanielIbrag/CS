#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Oct 5th 2023
#This program asks for user input then counts the words in the program, finally it counts the number of words that end in s
nouns = input("Enter a list of nouns: ")
nouns = nouns.split()
count = 0
for i in nouns:
    if i[-1] == "s":
        count += 1
print("Total number of words:", len(nouns))
print("Fraction that end in 's':", count/len(nouns))