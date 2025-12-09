#Day 9
import math

def is_prime(n):
    # to return true if n is true and false if not
    # 0 and 1 are not prime
    if n <= 1:
        return False
        
    # 2 and 3 are prime
    if n <= 3:
        return True
        
    # Check if divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    # Check for factors from 5 up to sqrt(n)
    # The loop step is 6 because all primes > 3 are of the form 6k ± 1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True

# Example Usage
print(f"Is 17 prime? {is_prime(17)}") 
print(f"Is 15 prime? {is_prime(15)}")


#Question 2
