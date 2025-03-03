def format_phone_number(nums: list[int]) -> str:
    """Returns a formatted phone number string based on a list of numbers in order

    Args:
        nums (list[int]): a list of numbers constituting a phone number

    Returns:
        str: a formated phone number (xxx) xxx-xxxx
    """
    first = "".join([str(i) for i in nums[:3]])
    second = "".join([str(i) for i in nums[3:6]])
    third = "".join([str(i) for i in nums[6:]])

    
    return f"({first}) {second}-{third}"

def main():
    """Handles test cases and pretty printing
    """
    test_cases = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [5, 1, 9, 5, 5, 5, 4, 4, 6, 8], [3, 4, 5, 5, 0, 1, 2, 5, 2, 7]]
    answers = ["(123) 456-7890", "(519) 555-4468", "(345) 501-2527"]

    for i in range(len(test_cases)):
        result = format_phone_number(test_cases[i])
        
        assert result == answers[i]

        print(f"""format_phone_number({test_cases[i]})
output = {result}\n""")

if __name__ == "__main__":
    main()