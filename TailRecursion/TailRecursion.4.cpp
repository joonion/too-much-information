#include <iostream>
using namespace std;

typedef unsigned long long LargeInteger;

/*
 Fibonacci sequence using the recursion
 */
LargeInteger fibo(LargeInteger n)
{
    if (n <= 1)
        return n;
    else
        return fibo(n - 1) + fibo(n - 2);
}

int main() 
{
    LargeInteger n;
    cin >> n;
    cout << fibo(n) << endl;
}
