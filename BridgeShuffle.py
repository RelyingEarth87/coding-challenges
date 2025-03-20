from typing import Any

def bridgeShuffle(arr1: list[Any], arr2: list[Any]) -> list[Any]:
    """Shuffles two lists together, alternating between elements from each list

    Args:
        arr1 (list[Any]): first list
        arr2 (list[Any]): second list

    Returns:
        list[Any]: shuffled list
    """
    shuffled = []

    while len(arr1) > 0 or len(arr2) > 0:
        if len(arr1) > 0:
            shuffled.append(arr1.pop(0))
        if len(arr2) > 0:
            shuffled.append(arr2.pop(0))
    
    return shuffled

def main():
    """Handles test cases and pretty printing
    """
    test_cases = [(["A", "A", "A"], ["B", "B", "B"]), (["C", "C", "C", "C"], ["D"]), ([1, 3, 5, 7], [2, 4, 6])]
    answers = [["A", "B", "A", "B", "A", "B"], ["C", "D", "C", "C", "C"], [1, 2, 3, 4, 5, 6, 7]]

    for i in range(len(test_cases)):
        arr1, arr2 = test_cases[i]
        result = bridgeShuffle(arr1.copy(), arr2.copy())
        
        assert result == answers[i]
        print(f"""bridgeShuffle({arr1, arr2})
output = {result}\n""")

if __name__ == "__main__":
    main()