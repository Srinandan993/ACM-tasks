#include <stdio.h>
#include <stdbool.h>

long long sumPrimes(int limit) {
    long long sum = 0;
    bool is_prime[limit];

    // Initialize all entries as true (prime)
    for (int i = 2; i < limit; i++) {
        is_prime[i] = true;
    }

    // Sieve of Eratosthenes
    for (int i = 2; i * i < limit; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j < limit; j += i) {
                is_prime[j] = false; // Mark multiples of i as non-prime
            }
        }
    }

    // Sum up all prime numbers
    for (int i = 2; i < limit; i++) {
        if (is_prime[i]) {
            sum += i;
        }
    }

    return sum;
}

int main() {
    const int limit = 2000000;
    long long result = sumPrimes(limit);
    printf("The sum of all primes below 2000000 is %lld\n", result);
    return 0;
}
