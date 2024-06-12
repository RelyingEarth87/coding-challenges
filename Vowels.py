def num_vowels(phrase: str) -> int:
    """A function that accepts a phrase and returns the number of vowels present

    Args:
        phrase (str): The user input string to determine the number of vowels

    Returns:
        int: the number of vowels present in user input string
    """

    import re

    vowels: list[str] = []

    a_s = re.findall('a', phrase)
    e_s = re.findall('e', phrase)
    i_s = re.findall('i', phrase)
    o_s = re.findall('o', phrase)
    u_s = re.findall('u', phrase)

    vowels += a_s + e_s + i_s + o_s + u_s

    return len(vowels)

def main() -> None:
    """Testing test cases for the num_vowels function
    """
    test_cases = ["Celebration", "Palm", "Prediction"]

    for i in test_cases:
        vowels = num_vowels(i)
        print(f"Number of vowels in {i}: {vowels}")


if __name__ == "__main__":
    main()