#include <iostream>
using namespace std;

typedef unsigned long long LargeInteger;

/*
 Summation to n using the tail recursion
 */
LargeInteger sum_to(LargeInteger n, LargeInteger m)
{
    if (n == 0)
        return m;
    else
        return sum_to(n - 1, n + m);
}

int main() 
{
    LargeInteger n;
    cin >> n;
    cout << sum_to(n, 0) << endl;
}

