def is_valid_hex_code(code: str) -> bool:
    """Determines if a string is a valid hex code

    Args:
        code (str): a string to be tested

    Returns:
        bool: True if string is a valid hex code; False otherwise
    """
    if code[0] != "#":
        return False
    
    if len(code) != 7:
        return False
    
    for i in code[1:]:
        if i.lower() not in "abcdef1234567890":
            return False
    
    return True

def main():
    test_cases = ["#CD5C5C", "#EAECEE", "#eaecee", "#CD5C58C", "#CD5C5Z", "#CD5C&C", "CD5C5C"]
    answers = [True, True, True, False, False, False, False]

    for i in range(len(test_cases)):
        result = is_valid_hex_code(test_cases[i])

        assert result == answers[i]

        print(f"""is_valid_hex_code("{test_cases[i]}")
output = {result}\n""")

if __name__ == "__main__":
    main()