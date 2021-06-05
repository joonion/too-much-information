#include <iostream>
using namespace std;

typedef unsigned long long LargeInteger;

/*
 Fibonacci sequence using the iteration
 */
LargeInteger fibo(LargeInteger n)
{
    if (n <= 1)
        return n;
    else {
        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            int t = b;
            b = a + b;
            a = t;
        }
        return b;
    }
}

int main() 
{
    LargeInteger n;
    cin >> n;
    cout << fibo(n) << endl;
}
