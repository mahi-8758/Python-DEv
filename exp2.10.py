"""Develop a program that takes numbers as input and calculates the
sum until it encounters a negative number, using the break statement."""
def sum_until_negative():
    """
    Calculates the sum of numbers entered by the user until a negative number is encountered.
    The negative number itself is not included in the sum.
    """
    total_sum = 0
    print("--- Sum Numbers Until Negative ---")
    print("Enter numbers one by one. The sum will be calculated until you enter a negative number.")

    while True:
        try:
            # Get input from the user
            user_input_str = input("Enter a number (or a negative number to stop): ")
            number = int(user_input_str)

            # Check if the number is negative
            if number < 0:
                print(f"Negative number ({number}) entered. Stopping sum calculation.")
                break  # Exit the loop if a negative number is entered
            else:
                total_sum += number
                print(f"Added {number}. Current sum: {total_sum}")

        except ValueError:
            print("Invalid input. Please enter a valid integer number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print(f"\nFinal sum of positive numbers entered: {total_sum}")

if __name__ == "__main__":
    sum_until_negative()


