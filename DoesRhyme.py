def doesRhyme(phrase1: str, phrase2: str) -> bool:
    """Determines whether or not two given phrases rhyme based on ending with the same characters

    Args:
        phrase1 (str): a string containing one or more words
        phrase2 (str): a string containing one or more words

    Returns:
        bool: True if the phrases rhyme (have the same endings), False otherwise
    """
    word1 = phrase1.split()[-1].strip(".,!?:;").lower()
    word2 = phrase2.split()[-1].strip(".,!?:;").lower()

    if word1.endswith(word2) or word2.endswith(word1):
        return True
    elif len(word1) < 3 or len(word2) < 3:
        return False
    elif word1.endswith(word2[1:]) or word2.endswith(word1[1:]):
        return True
    elif word1.endswith(word2[2:]) or word2.endswith(word1[2:]):
        return True

    return False

def main() -> None:
    """Handles test cases and pretty printing
    """
    test_cases = [("Sam I am!", "Green eggs and ham."), ("Sam I am!", "Green eggs and HAM."), ("You're built like a seat", "I bet you like to eat"),
("You are off to the races", "a splendid day."), ("and frequently do?", "you gotta move.")]
    answers = [True, True, True, False, False]

    for i in range(len(test_cases)):
        phrase1, phrase2 = test_cases[i]
        result = doesRhyme(phrase1, phrase2)

        assert result == answers[i]

        print(f"""doesRhyme({phrase1}, {phrase2})
output = {result}\n""")


if __name__ == "__main__":
    main()