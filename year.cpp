//Name: Daniel Ibragimov
//Date: 12/13/2023
//This program asks a user to enter a year and then prints it out.


#include <iostream>
using namespace std;

int main()
{
    int year;
    cout << "Enter a year: ";
    cin >> year;
    while (year > 2018)
    {
        cout << "Enter a year: ";
        cin >> year;
    }
    cout << "You entered:" << year << endl;
    return 0;
}