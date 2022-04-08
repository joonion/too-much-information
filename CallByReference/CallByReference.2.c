#include <stdio.h>

void swap(int *x, int *y);

int main() {
    
    int x = 10, y = 20;

    printf("Before swap(): %d %d\n", x, y);
    swap(&x, &y);
    printf("After swap(): %d %d\n", x, y);
}

void swap(int *x, int *y) {
    int t = *x;
    *x = *y;
    *y = t;
    printf("Inside swap(): %d %d\n", *x, *y);
}

