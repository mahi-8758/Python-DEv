def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
a, b = 1, 2
prime_sum = 0
while b < 2000000:
    if is_prime(b):
        prime_sum += b
    a, b = b, a + b
print(f"Sum of primes in Fibonacci sequence: {prime_sum}")