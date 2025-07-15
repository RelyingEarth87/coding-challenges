def findBrokenKeys(ideal: str, actual: str) -> list[str]:
    """Returns correct letters when given a correct phrase and an incorrectly typed one

    Args:
        ideal (str): the phrase that was attempted
        actual (str): what was typed

    Returns:
        list[str]: one instance of each correct letter that was written incorrectly
    """
    difference = []

    for i in range(len(ideal)):
        if ideal[i] != actual[i] and ideal[i] not in difference:
            difference.append(ideal[i])
    
    return difference

def main():
    test_cases = [("happy birthday", "hawwy birthday"), ("starry night", "starrq light"), ("beethoven", "affthoif5")]
    answers = [["p"], ["y", "n"], ["b", "e", "v", "n"]]

    for i in range(len(test_cases)):
        result = findBrokenKeys(test_cases[i][0], test_cases[i][1])

        assert result == answers[i]

        print(f"""findBrokenKeys{test_cases[i]} -> {result}\n""")

if __name__ == "__main__":
    main()