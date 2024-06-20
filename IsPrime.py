def isPrime(num: int) -> bool:
    """A function to check if a number is prime or not

    Args:
        num (int): the number to check

    Returns:
        bool: indicates True if the number is prime, False if composite
    """
    for i in range(2, round(num / 2) + 1):
        if num % i == 0:
            return False
        else:
            continue
    
    return True

def main() -> None:
    """Main entry point, asks user for a number to check if it is prime, returns a pretty-printed answer"""
    
    repeat = True
    while repeat == True:
        print("""Welcome to the prime number checker. Please enter a number to check if it is prime or composite.""")
        num = int(input("What number would you like to check? "))
        prime = isPrime(num)
        if prime == True:
            print(f"{num} is a prime number.")
        elif prime == False:
            print(f"{num} is a composite number")
        
        again = input("Would you like to check a different number? (y/n) ")
        if again.lower() == 'y':
            repeat = True
        elif again.lower() == 'n':
            repeat = False
            print("Goodbye!")
        else:
            print("I'll take that as a probably... So anyways...")


if __name__ == "__main__":
    main()