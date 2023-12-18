//Write a C++ program that converts kilometers to miles. Your program should prompt the user for the number of kilometers and then print out the number of miles.

//A useful formula: miles = 0.621371* kilometers.


#include <iostream>
using namespace std;

int main()
{
    double kilometers;
    double miles;
    cout << "Enter the number of kilometers: ";
    cin >> kilometers;
    miles = 0.621371 * kilometers;
    cout << kilometers << " kilometers is " << miles << " miles." << endl;
    return 0;
}