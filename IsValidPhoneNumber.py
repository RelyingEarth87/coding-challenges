def isValidPhoneNumber(test: str) -> bool:
    """Specifies if a given string is a valid phone number

    Args:
        test (str): the string to test

    Returns:
        bool: True if string is valid as a phone number, False otherwise
    """
    import re

    pattern = r"\([0-9]{3}\) [0-9]{3}-[0-9]{4}"
    if re.match(pattern, test):
        return True
    else:
        return False

def main():
    """Handles running test cases and pretty printing
    """
    test_cases = ["(123) 456-7890", "1111)555 2345", "098) 123 4567"]
    answers = [True, False, False]

    for i in range(len(test_cases)):
        result = isValidPhoneNumber(test_cases[i])
        assert result == answers[i]

        print(f"isValidPhoneNumber({test_cases[i]}) -> {result}")

if __name__ == "__main__":
    main()