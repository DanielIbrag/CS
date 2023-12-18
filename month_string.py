# Name:Daniel Ibragimov
# Date: nov 8th 2023
# A program that uses functions to print out months.

def monthString(monthNum):
     
     monthString = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

     

     return(monthString[int(monthNum)-1])

def main():
     n = int(input('Enter the number of the month: '))
     mString = monthString(n)
     print('The month is', mString)

#Allow script to be run directly:
if __name__ == "__main__":
     main()