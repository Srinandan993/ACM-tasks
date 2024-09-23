#include <stdio.h>

int sumEvenFibonacci(int limit) {
    int a = 0, b = 1, c;
    int sum = 0;

    while (1) {
        c = a + b; // Next Fibonacci number
        if (c >= limit) {
            break;
        }
        if (c % 2 == 0) {
            sum += c; // Add to sum if even
        }
        a = b; // Update for next iteration
        b = c;
    }
    return sum;
}

int main() {
    int limit;
    printf("Enter the limit for Fibonacci numbers: ");
    scanf("%d", &limit);
    int sum = sumEvenFibonacci(limit);
    printf("Sum of even Fibonacci numbers less than %d is %d\n", limit, sum);
    return 0;
}
