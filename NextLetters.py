def next_letters(letters: str) -> str:
    """Takes the last letter of a string and rolls it over to the next letter (Z back to A), repeating the process if the letter is a Z

    Args:
        letters (str): a sequence of capitalized, alphabetic characters

    Returns:
        str: A string where one or more letters was changed to be one later in the alphabet than before
    """
    if letters == "":
        return "A"

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    i = len(letters) - 1
    while i >= 0:
        num = alphabet.find(letters[i])
        new_letter = alphabet[(num+1)%26]
        letters = letters[:i] + new_letter + letters[i+1:]

        if num == 25 and i > 0:
            i -= 1
        elif num == 25:
            return "A" + letters
        else:
            return letters

def main():
    test_cases = ["A", "ABC", "Z", "CAZ", ""]
    answers = ["B", "ABD", "AA", "CBA", "A"]

    for i in range(len(test_cases)):
        result = next_letters(test_cases[i])

        assert result == answers[i]

        print(f"""next_letters("{test_cases[i]}")
output = "{result}"\n""")

if __name__ == "__main__":
    main()