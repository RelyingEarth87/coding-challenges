def find_first_occurrence(arr: list[int], target: int) -> int:
    """Returns the first occurrence of a target integer from a sorted list of integers using binary search

    Args:
        arr (list): a sorted list of integers
        target (int): an integer to search for in the target list

    Returns:
        int: returns the first occurrence of target in arr or -1 if no such occurrence is found
    """    
    first = 0
    last = len(arr) - 1
    midpoint = (last - first) // 2

    indexes_found = []

    while midpoint > 0:
        if target == arr[midpoint]:
            indexes_found.append(midpoint)
            last = midpoint - 1
        elif target > arr[midpoint]:
            first = midpoint + 1
        elif target < arr[midpoint]:
            last = midpoint - 1

        midpoint = (last - first) // 2

    if len(indexes_found) == 0:
        return -1
    first_index = min(indexes_found)

    return first_index

def main():
    """Main entry point to handle test cases set forth by SlothBytes' weekly mailing list challenge
    """
    #Input:
    arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]

    target = 3

    print(f"Case 1 = {find_first_occurrence(arr, target)} # Returns 1") # Return 1

    #Explanation: The first occurrence of 3 is at index 1.

    #Input:

    arr = [2, 3, 5, 7, 11, 13, 17, 19]

    target = 6
    print(f"Case 2 = {find_first_occurrence(arr, target)} # Returns -1") # Return -1

    #Explanation: 6 does not exist in the array.

    # another test case to check if the while loop holds up with an odd-sized list
    arr = [2, 3, 4, 5, 7, 11, 13, 17, 19]

    target = 6
    print(f"Case 3 = {find_first_occurrence(arr, target)} # Returns -1") # Return -1

    # another test case to check if the function works with a longer list since in case #1, at least one of the matches is skipped
    arr = [1, 2, 3, 3, 3, 3, 6, 10, 10, 10, 100]

    target = 3

    print(f"Case 4 = {find_first_occurrence(arr, target)} # Returns 2") # Return 2

if __name__ == '__main__':
    main()