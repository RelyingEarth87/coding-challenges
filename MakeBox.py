def makeBox(side_len: int) -> list[str]:
    """Makes an empty box, denoted with #s

    Args:
        side_len (int): the size of the square box to make

    Returns:
        list[str]: a list object containing strings used to construct the box
    """
    # returning an empty list if the box length is not a positive integer
    if side_len <= 0:
        return []
    
    box = []
    for i in range(side_len):
        # constructing top and bottom sides of box
        if i == 0 or i == side_len - 1:
            side_x = ''.join(["#" for x in range(side_len)])
            box.append(side_x)
        # constructing left and right sides of box
        else:
            side_x = '#' + ''.join([" " for x in range(side_len - 2)])
            side_x += "#"
            box.append(side_x)
    return box

def main() -> None:
    """A main entry point that handles test cases and printing output
    """
    # testing the results against their answers
    test_cases = [makeBox(5), makeBox(3), makeBox(2), makeBox(1)]
    answers = [["#####", "#   #", "#   #", "#   #", "#####"], ["###", "# #", "###"], ["##", "##"], ["#"]]
    assert test_cases == answers

    # pretty printing the results
    # I know this is convoluted, but print(*testCase, sep="\n") just wasn't quite right
    for testCase in test_cases:
        print(f"makeBox({len(testCase)}) -> [")
        for i in testCase:
            print(f'"{i}",')
        print(f"] {len(testCase)}x{len(testCase)} box\n")

if __name__ == "__main__":
    main()