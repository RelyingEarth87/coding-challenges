def isShuffledWell(nums: list[int]) -> bool:
    """Determines whether or not an array of 10 numbers is shuffled enough (does not have more than 2 consecutive integers adjacent to one another)

    Args:
        nums (list[int]): randomly shuffled list of 10 integers

    Returns:
        bool: True if shuffled list does not have more than 2 consecutive integers adjacent to one another; False otherwise
    """
    counter = 0
    i = 0
    while i < len(nums) - 1:
        if nums[i] + 1 == nums[i+1]:
            counter += 1
        elif nums[i] - 1 == nums[i+1]:
            counter -= 1
        else:
            counter = 0

        if counter == 2 or counter == -2:
            return False

        i += 1

    return True

def main():
    test_cases = [[1, 2, 3, 5, 8, 6, 9, 10, 7, 4], [3, 5, 1, 9, 8, 7, 6, 4, 2, 10], [1, 5, 3, 8, 10, 2, 7, 6, 4, 9], [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]]
    answers = [False, False, True, True]

    for i in range(len(test_cases)):
        result = isShuffledWell(test_cases[i])

        assert result == answers[i]

        print(f"""isShuffledWell({test_cases[i]})
output = {result}\n""")

if __name__ == "__main__":
    main()