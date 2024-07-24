def checkTitle(phrase: str) -> bool:
    """Checks if a string is formatted as a title (first letter of each word is capitalized)

    Args:
        phrase (str): A string to check

    Returns:
        bool: True if the string is formatted as a title, False otherwise
    """
    title = phrase.title()
    if phrase == title:
        return True
    
    return False

def main() -> None:
    """A main entry point to handle test cases and printing results in a readable format
    """
    test_cases = ["A Mind Boggling Achievement", "A Simple C++ Program!", "Water is transparent"]
    expected_outputs = [True, True, False]
    outputs = []
    
    for i in range(len(test_cases)):
        outputs.append(checkTitle(test_cases[i]))
        assert outputs[i] == expected_outputs[i]
        print(f"checkTitle({test_cases[i]}) -> {outputs[i]} \n")

if __name__ == "__main__":
    main()