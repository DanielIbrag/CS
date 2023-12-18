//Name: Daniel Ibragimov
//Date: 12/13/2023
// This program converts a number between -31 and 31 to binary


#include <iostream>
using namespace std;


int main()
{
    int n;
    cout << "Please enter a number between -31 and 31: ";
    cin >> n;
    if (n < 0)
    {
        cout << "1";
        n = 32 + n;
    }
    else
    {
        cout << "0";
    }
    int b = 16;
    while (b > 0.5)
    {
        if (n >= b)
        {
            cout << "1";
            n = n % b;
        }
        else
        {
            cout << "0";
        }
        b = b/2;
    }
    cout << endl;
    return 0;
}



