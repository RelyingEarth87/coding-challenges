def countSmileys(arr: list[str]) -> int:
    """Distinguishes and counts the number of smiley faces in a given list

    Args:
        arr (list[str]): A list of strings containing special characters in the form of faces

    Returns:
        int: The count of smiley faces in the given list
    """
    eyes = [":", ";"]
    nose = ["-", "~"]
    mouth = [")", "D"]

    count = 0
    for i in arr:
        if len(i) == 3 and i[1] not in nose:
            continue
        elif i[0] in eyes and i[-1] in mouth:
            count += 1
    
    return count

def main():
    """A main entry point to handle test cases and pretty printing
    """
    cases = [[":)", ";(", ";}", ":-D"], [";D", ":-(", ":-)", ";~)"], [";]", ":[", ";*", ":$", ";-D"], [], [":=)"]]

    for i in cases:
        print(f"countSmileys({i}) -> {countSmileys(i)}")

if __name__ == "__main__":
    main()