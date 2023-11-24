#include <iostream>
#include <cmath>


int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    // Your code goes here
    
    return 0;
}
