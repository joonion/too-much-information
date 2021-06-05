#include <iostream>
using namespace std;

typedef unsigned long long LargeInteger;

/*
 Summation to n using the recursion
 */
LargeInteger sum_to(LargeInteger n)
{
    if (n == 1)
        return 1;
    else
        return n + sum_to(n - 1);
}

int main() 
{
    LargeInteger n;
    cin >> n;
    cout << sum_to(n) << endl;
}