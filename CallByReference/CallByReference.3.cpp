#include <iostream>
using namespace std;

void swap(int &x, int &y) {
    int t = x;
    x = y;
    y = t;
    cout << "Inside swap(): " << x << " " << y << endl;
}

int main() {
    int x = 10, y = 20;

    cout << "Before swap(): " << x << " " << y << endl;
    swap(x, y);
    cout << "After swap(): " << x << " " << y << endl;
}