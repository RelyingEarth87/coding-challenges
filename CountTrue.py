def countTrue(arr: list) -> int:
    """Takes an array of boolean values and returns the number of True values

    Args:
        arr (list): an array of boolean values

    Returns:
        int: the number of True values in arr
    """
    total = 0
    for i in arr:
        if i == True:
            total += 1
    return total

def main():
    """A main function to handle the test cases and pretty printing of output
    """
    test_cases = [[True, False, False, True, False], [False, False, False, False], []]
    answers = [2, 0, 0]

    for i in range(len(test_cases)):
        assert countTrue(test_cases[i]) == answers[i]

        print(f"countTrue({test_cases[i]}) -> {countTrue(test_cases[i])} \n")

        
if __name__ == '__main__':
    main()