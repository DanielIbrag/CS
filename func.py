#Write a function that asks a user for number after 2000 but before 2021.The function should repeatedly ask the user for a number until they enter one within the range and return the number.

def getYear():
    year = int(input("Enter a year after 2000 but before 2021: "))
    while year < 2000 or year > 2021:
        year = int(input("Enter a year after 2000 but before 2021: "))
    return year

getYear()