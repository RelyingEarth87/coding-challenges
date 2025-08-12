def maximumSeating(row: list[int]) -> int:
    """Returns the number of available seats in a theater row (new guests must have 2 empty seats between them and previously sat guests)

    Args:
        row (list[int]): A theater row where empty seats are represented by the number 0 and occupied seats are 1

    Returns:
        int: The current number of seats available in the row with 2 spaces between them and the nearest seated guest
    """
    row_copy = row.copy()

    available = 0
    for i in range(len(row_copy)):
        if row_copy[i] == 1:
            continue
        else:
            lst = []
            for j in range(i-2, i+3):
                if j < 0 or j >= len(row_copy):
                    pass
                else:
                    lst.append(row_copy[j])
            if 1 in lst:
                continue
            else:
                available += 1
                row_copy[i] = 1

    return available

def main():
    test_cases = [[0, 0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    answers  = [2, 2, 0, 2, 4]

    for i in range(len(test_cases)):
        result = maximumSeating(test_cases[i])

        assert result == answers[i]

        print(f"""maximumSeating({test_cases[i]})
output = {result}\n""")

if __name__ == "__main__":
    main()