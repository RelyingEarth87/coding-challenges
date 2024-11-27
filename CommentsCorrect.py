def comments_correct(slashes: str) -> bool:
    """Takes a string and returns a boolean indicating whether it contains valid JavaScript comments

    Args:
        slashes (str): a string of slashes (/) or asterisks (*)

    Returns:
        bool: True if string contains character that could be valid JavaScript comments; False otherwise
    """
    multi1 = "/*"
    multi2 = "*/"
    single = "//"

    arr = list(slashes)
    i = 0
    multi1_hanging = 0
    while i < len(arr):
        if i + 1 >= len(arr):
            return False
        elif arr[i] + arr[i + 1] == single:
            arr.pop(i)
            arr.pop(i)
        elif arr[i] + arr[i + 1] == multi1:
            multi1_hanging += 1
            arr.pop(i)
            arr.pop(i)
        elif arr[i] + arr[i + 1] == multi2:
            if multi1_hanging == 0:
                return False
            multi1_hanging -= 1
            arr.pop(i)
            arr.pop(i)
        else:
            return False
    if multi1_hanging != 0:
        return False
    return True

def main():
    test_cases = ["//////", "/**//**////**/", "///*/**/", "/////"]
    answers = [True, True, False, False]

    for i in range(len(test_cases)):
        result = comments_correct(test_cases[i])
        assert result == answers[i]

        print(f"comments_correct({test_cases[i]}) -> {result}")

if __name__ == "__main__":
    main()