def birthdayCakeCandles(candles: list[int]) -> int:
    """Takes a list of candle heights and returns the number of the tallest length candles

    Args:
        candles (list[int]): a list of integers representing candle height

    Returns:
        int: the count of the tallest length candles
    """
    if candles == []:
        return 0
    
    tallest = max(candles)

    return candles.count(tallest)

def main():
    test_cases = [[4,4,1,3], [1, 1, 1, 1], []]
    answers = [2, 4, 0]

    for i in range(len(test_cases)):
        result = birthdayCakeCandles(test_cases[i])

        assert result == answers[i]

        print(f"""birthdayCakeCandles({test_cases[i]})
output = {result}\n""")

if __name__ == "__main__":
    main()