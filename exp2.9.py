"""Write a program to calculate the sum of all prime numbers within a
given range (input by the user)."""
def is_prime(num):
    """
    Checks if a given number is prime.

    A number is prime if it is greater than 1 and has no positive divisors
    other than 1 and itself.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if num <= 3:
        return True   # 2 and 3 are prime numbers
    if num % 2 == 0 or num % 3 == 0:
        return False  # Multiples of 2 or 3 are not prime

    # Check for prime by iterating from 5 with a step of 6
    # All primes greater than 3 can be expressed in the form 6k ± 1
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def sum_primes_in_range(start, end):
    """
    Calculates the sum of all prime numbers within a specified range.

    Args:
        start (int): The beginning of the range (inclusive).
        end (int): The end of the range (inclusive).

    Returns:
        int: The sum of prime numbers in the range.
    """
    if start > end:
        print("Warning: Start of the range is greater than the end. Swapping values.")
        start, end = end, start # Swap if start is greater than end

    prime_sum = 0
    print(f"Checking for prime numbers between {start} and {end}...")
    for number in range(start, end + 1):
        if is_prime(number):
            prime_sum += number
            print(f"Found prime: {number}") # Optional: print found primes
    return prime_sum


if __name__ == "__main__":
    print("--- Prime Number Sum Calculator ---")
    while True:
        try:
            # Get the start of the range from the user
            start_range_str = input("Enter the starting number of the range: ")
            start_range = int(start_range_str)

            # Get the end of the range from the user
            end_range_str = input("Enter the ending number of the range: ")
            end_range = int(end_range_str)

            # Validate input: Ensure numbers are non-negative
            if start_range < 0 or end_range < 0:
                print("Please enter non-negative numbers for the range.")
                continue

            # Calculate the sum of primes
            total_sum = sum_primes_in_range(start_range, end_range)

            # Print the result
            print(f"\nThe sum of all prime numbers between {min(start_range, end_range)} and {max(start_range, end_range)} is: {total_sum}")
            break # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter valid integer numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

