def canJump(nums: list[int]) -> bool:
    """Uses the numbers in a list as jump lengths and jumps across the list of numbers

    Args:
        nums (list[int]): a list of numbers

    Returns:
        bool: True if able to traverse the whole list, False otherwise
    """
    curr = 0
    if 0 not in nums:
        return True
    while curr < len(nums):
        if nums[curr] == 0:
            return False
        curr += nums[curr]

    return True

def main():
    test_cases = [[2,3,1,1,4], [3,2,1,0,4], [3,2,0,1,4]]
    answers = [True, False, True]

    for i in range(len(test_cases)):
        result = canJump(test_cases[i])

        assert result == answers[i]

        print(f"canJump({test_cases[i]}) -> {result}\n")

if __name__ == "__main__":
    main()