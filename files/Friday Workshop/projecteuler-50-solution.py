#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def isPrime(n):
    if n == 2:
        return True;
    if n < 2 or n % 2 == 0:
        return False
    f = 3
    while f * f <= n:
        if n % f == 0:
            return False
        f += 2
    return True

primes = [p for p in range(20000) if isPrime(p)]

max_sum = 1000000
sum_of_longest_list_of_primes = 0
number_of_primes_in_longest_list = 0
starting_index = 0
while True:
    # iterate over the starting primes (2, then 3, etc)
    prime_index = starting_index
    if number_of_primes_in_longest_list * primes[prime_index] > max_sum:
        break
    
    sum_of_p = 0
    prime_count = 0
    
    while sum_of_p < max_sum:
        # find longest sum starting with the starting prime
        prime = primes[prime_index]
        sum_of_p += prime
        prime_count += 1
        if prime_count > number_of_primes_in_longest_list and \
        isPrime(sum_of_p):
            if sum_of_p < max_sum:
                number_of_primes_in_longest_list = prime_count
                sum_of_longest_list_of_primes = sum_of_p
        prime_index += 1
    
    starting_index += 1
print(number_of_primes_in_longest_list, sum_of_longest_list_of_primes)

