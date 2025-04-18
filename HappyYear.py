def happyYear(year: int) -> int:
    """Takes a year as an input and returns the next year that has all unique component digits

    Args:
        year (int): a given 4-digit year

    Returns:
        int: a 4-digit year after the input year that has 4 unigue digits
    """
    year += 1
    sep = [i for i in str(year)]

    set_ = set(sep)

    while len(set_) < len(sep):
        year += 1
        sep = [i for i in str(year)]
        set_ = set(sep)
    
    print(year)
    return year

def main():
    """Handles test cases and pretty printing output
    """
    test_cases = [2017, 1990, 2021]
    answers = [2018, 2013, 2031]

    for i in range(len(test_cases)):
        result = happyYear(test_cases[i])

        assert result == answers[i]

        print(f"""happyYear({test_cases[i]})
output = {result}\n""")

if __name__ == "__main__":
    main()