#include <stdio.h>

int sumOfSquares(int n) {
    if (n == 0) return 0;
    return n * n + sumOfSquares(n - 1);
}

int sum(int n) {
    if (n == 0) return 0;
    return n + sum(n - 1);
}

int calculateDifference(int limit) {
    int sumOfSquaresValue = sumOfSquares(limit);
    int sumValue = sum(limit);
    int squareOfSum = sumValue * sumValue;
    return squareOfSum - sumOfSquaresValue;
}

int main() {
    int limit = 100;
    int difference = calculateDifference(limit);
    printf("The required result is %d\n", difference);
    return 0;
}
