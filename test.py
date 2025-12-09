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

def find_missing_number(arr):
    """
    Finds the missing number in an array of integers from 1 to n.
    
    Args:
        arr (list): A list of integers missing one number from the range [1, n].
        
    Returns:
        int: The missing number.
    """
    # n is the expected size of the list if no number was missing
    # so n is the maximum number in the range.
    n = len(arr) + 1 
    
    # 1. Calculate the expected sum (Sum of 1 to n)
    # Formula: n * (n + 1) / 2
    expected_sum = n * (n + 1) // 2
    
    # 2. Calculate the actual sum of the elements in the given array
    actual_sum = sum(arr)
    
    # 3. The difference is the missing number
    missing_num = expected_sum - actual_sum
    
    return missing_num

# Example Usage
my_array = [1, 2, 4, 6, 3, 7, 8] # n=8, missing 5
missing = find_missing_number(my_array)
print(f"The missing number in {my_array} is: {missing}")

# this is a comment