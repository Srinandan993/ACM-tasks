#include <stdio.h>

int sumOfMultiples(int limit) {
    int sum = 0;
    for (int i = 0; i < limit; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    int limit = 1000;
    int result = sumOfMultiples(limit);
    printf("The sum of the multiples of 3 and 5 below %d is %d\n", limit, result);
    return 0;
}
