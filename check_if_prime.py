def check_if_prime(n:int) -> bool:
    """Check if the input number n is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def find_primes(limit:int) -> list:
    """Return a list of prime numbers up to the given limit."""
    primes = []
    for num in range(2, limit + 1):
        if check_if_prime(num):
            primes.append(num)
    return primes

# number = int(input("Enter a number to check if prime: "))
# if check_if_prime(number):
#     print(f"{number} is a prime number.")   
number_limit = int(input("Enter a limit to find all prime numbers up to that limit: "))
prime_numbers = find_primes(number_limit)
print(f"Prime numbers up to {number_limit}:", prime_numbers)      
