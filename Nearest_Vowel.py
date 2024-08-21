def nearest_vowel(letter: str) -> str:
    """Takes a letter of the alphabet and returns its closest vowel (earliest vowel first if tie)

    Args:
        letter (str): A single alphabetical letter for which to find nearest vowel

    Returns:
        str | None: Returns a string containing the closest vowel (earliest first) to the given letter
    """
    import string
    vowels = ["a", "e", "i", "o", "u"]
    letters = string.ascii_lowercase
    if letter.lower() in vowels:
        return letter.lower()
    
    is_solved = False
    index = letters.find(letter.lower())
    if index == -1:
        return None
    start = index - 1
    end = index + 1
    while not is_solved:
        try:
            if letters[start] in vowels:
                is_solved = True
                return letters[start]
        except IndexError:
            pass
        try:
            if letters[end] in vowels:
                is_solved = True
                return letters[end]
        except IndexError:
            pass
        start -= 1
        end += 1

        if start < 0 and end > 25:
            is_solved = True
            break
    return None


def main():
    """ Main entry point into the program that handles test cases and pretty printing
    """
    test_cases = ["b", "s", "c", "i", "z", "D", "4"]
    answers = ["a", "u", "a", "i", "u", "e", None]

    for i in range(len(test_cases)):
        assert nearest_vowel(test_cases[i]) == answers[i]
        print(f"""nearest_vowel({test_cases[i]})
output = {nearest_vowel(test_cases[i])}""")

if __name__ == '__main__':
    main()