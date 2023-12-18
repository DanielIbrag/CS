//Name: Daniel Ibragimov
//Date: 12/13/2023
#include <iostream>
using namespace std;

int main()
{
    double p = 325.7;
    double B = 12.4;
    double D = 8.4;
    int years;
    cout << "Please enter the number of years: ";
    cin >> years;
    for (int i = 0; i <= years; i++)
    {
        cout << "Year " << 2017 + i << " " << p << endl;
        p = p + (B/1000)*p - (D/1000)*p;
    }
    return 0;
}
