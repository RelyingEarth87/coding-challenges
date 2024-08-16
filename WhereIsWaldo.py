def whereIsWaldo(arr: list[str]) -> list[int]:
    import statistics
    for i in range(len(arr)):
        if len(set(arr[i])) == 2:
            row = i + 1
            break
    
    mode = statistics.mode(arr[i])
    for j in range(len(arr[i])):
        if arr[i][j] != mode:
            col = j + 1
            break
    
    return [row, col]


def main() -> None:
    test_cases = [[["A", "A", "A"], ["A", "A", "A"], ["A", "B", "A"]], [["c", "c", "c", "c"], ["c", "c", "c", "d"]], [["O", "O", "O", "O"], ["O", "O", "O", "O"], ["O", "O", "O", "O"], ["O", "O", "O", "O"], ["P", "O", "O", "O"], ["O", "O", "O", "O"]]]
    answers = [[3, 2], [2, 4], [5, 1]]

    for i in range(len(test_cases)):
        assert whereIsWaldo(test_cases[i]) == answers[i]

        print(f"""whereIsWaldo({test_cases[i]})
output = {whereIsWaldo(test_cases[i])} \n""")

if __name__ == "__main__":
    main()