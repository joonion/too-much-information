#include <iostream>
using namespace std;

typedef unsigned long long LargeInteger;

/*
 Summation to n using the iteration
 */
LargeInteger sum_to(LargeInteger n)
{
    LargeInteger s = 0;
    for (LargeInteger i = 1; i <= n; i++)
        s += i;
    return s;
}

int main() 
{
    int n;
    cin >> n;
    cout << sum_to(n) << endl;
}