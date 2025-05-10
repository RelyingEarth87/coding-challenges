def noYelling(message: str) -> str:
    """Takes a string and removes excess ? and ! punctuation at the end

    Args:
        message (str): a sentence that may or may not have punctuation at the end

    Returns:
        str: the sentence, minus extra punctuation 
    """
    symbols = ["?", "!"]

    i = -1
    counter = 0

    while i >= (0 - len(message)):
        if message[i] in symbols:
            counter += 1
        if message[i] not in symbols and counter > 1:
            return message[:i+2]
        i -= 1

    return message

def main():
    test_cases = ["What went wrong?????????", "Oh my goodness!!!", "I just!!! can!!! not!!! believe!!! it!!!", "Oh my goodness!", "Oh my goodness"]
    answers = ["What went wrong?", "Oh my goodness!", "I just!!! can!!! not!!! believe!!! it!", "Oh my goodness!", "Oh my goodness"]

    for i in range(len(test_cases)):
        result = noYelling(test_cases[i])

        assert result == answers[i]

        print(f"""noYelling({test_cases[i]})
output = {result}\n""")


if __name__ == "__main__":
    main()