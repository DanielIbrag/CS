//Name: Daniel Ibragimov
//Date: 12/08/23
//Convert kilos to miles


#include <iostream>
using namespace std;

int main()
{
    float kilometers;
    float miles;
    cout << "Enter the number of kilometers: ";
    cin >> kilometers;
    miles = 0.621371 * kilometers;
    cout << kilometers << " kilometers equal to" << miles << " miles." << endl;
    return 0;
}