def overlap(word1: str, word2: str) -> str:
    """Returns the shortest overlapped string possible made from two given words

    Args:
        word1 (str): The word to start the overlap
        word2 (str): The ending word

    Returns:
        str: A single string with no spaces showing the two words overlapped (or just concatenated if there is no overlap)
    """
    i = 0
    while i < len(word1):
        if word1[i:] in word2:
            return word1[:i] + word2
        i += 1
    return word1 + word2


def main():
    test_cases = [("sweden", "denmark"), ("honey", "milk"), ("dodge", "dodge")]
    answers = ["swedenmark", "honeymilk", "dodge"]

    for i in range(len(test_cases)):
        result = overlap(test_cases[i][0], test_cases[i][1])

        assert result == answers[i]

        print(f"""overlap{test_cases[i]}
output = "{result}"\n""")

if __name__ == "__main__":
    main()