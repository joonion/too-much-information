#include <iostream>
using namespace std;

typedef unsigned long long LargeInteger;

/*
 Fibonacci sequence using the tail recursion
 */
LargeInteger helper(LargeInteger limit, LargeInteger a, LargeInteger b) {
    if (limit == 0)
        return a;
    else if (limit == 1)
        return b;
    else
        return helper(limit - 1, b, a + b);
}

LargeInteger fibo(LargeInteger n)
{
    return helper(n, 0, 1);
}

int main() 
{
    LargeInteger n;
    cin >> n;
    cout << fibo(n) << endl;
}
