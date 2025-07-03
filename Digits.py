def digits(num: int) -> int:
    """Finds how many digits exist in a string with all digits between 0 and a number (non-inclusive)

    Args:
        num (int): an integer greater than 0

    Returns:
        int: the number of digits between 0 and num in a concatenated list
    """
    result = ""

    for i in range(1, num):
        str_num = str(i)
        result = result + str_num

    return len(result)

def main():
    test_cases = [1, 10, 100, 2020]
    answers = [0, 9, 189, 6969]

    for i in range(len(test_cases)):
        result = digits(test_cases[i])

        assert result == answers[i]

        print(f"""digits({test_cases[i]})
output = {result}\n""")

if __name__ == "__main__":
    main()