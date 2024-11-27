def num_split(val: int) -> list[int]:
    """Takes an integer and returns a list of the values of each digit in its place in the value

    Args:
        val (int): an integer

    Returns:
        list[int]: a list of the place values of each digit in the value
    """
    splt: list[int] = []

    string = str(val)

    if string[0] == '-':
        sign = -1
        string.replace("-", "")
    else:
        sign = 1

    for i in range(len(string) - 1, -1, -1):
        if string[i] == '-':
            break
        digit = string[i]
        splt.insert(0, int(digit) * (10**(len(string) - i - 1)) * sign)
    
    return splt

def main():
    """A main function that handles the test cases and pretty printing
    """
    test_cases = [39, -434, 100]
    answers = [[30, 9], [-400, -30, -4], [100, 0, 0]]

    for i in range(len(test_cases)):
        result = num_split(test_cases[i])
        assert result == answers[i]
        print(f"num_split({test_cases[i]}) -> {result}\n")


if __name__ == "__main__":
    main()