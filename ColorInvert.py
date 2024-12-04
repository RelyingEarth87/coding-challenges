def color_invert(color: list[int]) -> list[int]:
    opposite = [];

    for i in color:
        opposite.append(255-i)

    return opposite

def main():
    test_cases = [[255, 255, 255], [0, 0, 0], [165, 170, 221]]
    answers = [[0, 0, 0], [255, 255, 255], [90, 85, 34]]

    for i in range(len(test_cases)):
        result = color_invert(test_cases[i])
        assert result == answers[i]

        print(f"color_invert({test_cases[i]}) -> {result}")

if __name__ == '__main__':
    main()