# This algo will give a set of prime number in given a range.
# The idea is to mark the multiple of a number as False as we iterate over the number which are marked as True and append that number into a list.
# Start with creating an array of True bool value of size given.

def generate_prime(n=10):
    if n < 2:
        return []

    sieve = [False, False] + [True] * (n-1)

    for i in range(2, n+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    
    return [i for i in range(n) if sieve[i]]


# To check if a number is prime or not
def is_prime(n=21):
    
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    
    return n != 1

print(is_prime())



