def spiralOrder(rect: list[list[int]]) -> list[int]:
    """Returns the numbers in a matrix in spiral order

    Args:
        square (list[list[int]]): a matrix of indices in a rectangle shape

    Returns:
        list[int]: a list of the items in the matrix, listed out in a spiral shape
    """
    from copy import deepcopy
    directions = {"right": (0, 1), "down": (1, 0), "left": (0, -1), "up": (-1, 0)}
    options: list[str] = list(directions.keys())
    direction = "right"
    copied = deepcopy(rect)

    start = (0, 0)
    spiral = [copied[start[0]][start[1]]]
    copied[0][0] = "."
    pos = start

    finished = False
    while not finished:
        curr_dir = directions[direction]
        next_ = (pos[0]+curr_dir[0], pos[1]+curr_dir[1])

        try:
            if copied[next_[0]][next_[1]] == ".":
                direction = options[(options.index(direction)+1)%len(options)]
            elif next_[0] < 0 or next_[1] < 0:
                direction = options[(options.index(direction)+1)%len(options)]
            else:
                copied[pos[0]][pos[1]] = "."
                pos = next_
                spiral.append(copied[pos[0]][pos[1]])
        except IndexError:
            direction = options[(options.index(direction)+1)%len(options)]


        if len(spiral) == (len(copied[0]) * len(copied)):
            finished = True
            break

    return spiral

def main():
    test_cases = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]
    answers = [[1, 2, 3, 6, 9, 8, 7, 4, 5], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]]

    for i in range(len(test_cases)):
        result = spiralOrder(test_cases[i])

        assert result == answers[i]

        print(f"""spiralOrder({test_cases[i]})
output = {result}\n""")

if __name__ == "__main__":
    main()