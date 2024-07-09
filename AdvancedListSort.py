def advanced_sort(unsorted: list[any]) -> list[list]:
    """Sorts an unsorted list into sub lists of the same value

    Args:
        unsorted (list): an unsorted list of type str or int

    Returns:
        list[list]: a list of sorted sublists containing the same value
    """
    # copying the original list so not removing the data when printing later
    unsorted = unsorted.copy()
    # creating a lookup so no need for nested for loops
    used: dict = {}
    sorted_list: list = []

    while len(unsorted) > 0:
        i = unsorted.pop(0)
        if i not in used.keys():
            used[i] = len(sorted_list)
            sorted_list.append([i])
        else:
            sorted_list[used[i]].append(i) 

    return sorted_list

def main() -> None:
    """Main entry point to handle test cases and outputting results
    """
    test_cases: list = [[2, 1, 2, 1], [5, 4, 5, 5, 4, 3], ["b", "a", "b", "a", "c"]]
    answers: list = ["[[2, 2], [1, 1]]", "[[5, 5, 5], [4, 4], [3]]", r"[['b', 'b'], ['a', 'a'], ['c']]"]
    
    for i in range(len(test_cases)):
        case_i = advanced_sort(test_cases[i])
        assert str(case_i) == answers[i]
        print(f"\nadvanced_sort({test_cases[i]}) -> {case_i}")

if __name__ == '__main__':
    main()