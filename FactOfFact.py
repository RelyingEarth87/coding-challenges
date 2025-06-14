import math

def fact_of_fact(num: int) -> int:
    """Recursive function to determine the factorial of factorials of a given integer (>0)

    Args:
        num (int): a positive integer, greater than 0

    Returns:
        int: factorial of factorials of a given integer (num! * (num-1)! * (num-2)!...)
    """
    if num == 1:
        return 1
    else:
        return math.factorial(num) * fact_of_fact(num-1)

def main():
    test_cases = [4, 5, 6]
    answers = [288, 34560, 24883200]

    for i in range(len(test_cases)):
        result = fact_of_fact(test_cases[i])

        assert result == answers[i]
        print(f"""fact_of_fact({test_cases[i]})
output = {result}\n """)

if __name__ == "__main__":
    main()