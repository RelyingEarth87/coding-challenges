def simon_says(ins: list[str]) -> int:
    """Takes a list of instructions and returns a number after the instructions are performed on the starting number, 0, only when the instructions start with Simon Says

    Args:
        ins (list[str]): a list of mathematical instructions

    Returns:
        int: a number after some mathematical operations, 0 if no operations performed
    """
    num = 0
    key = "Simon says"
    
    for i in ins:
        if key not in i:
            continue
        chopped = i.split(" ")
        if "add" in i:
            num += int(chopped[-1])
        elif "subtract" in i:
            num -= int(chopped[-1])
        elif "multiply" in i:
            num *= int(chopped[-1])
    
    return num

def main():
    """
    A main function to handle test cases and pretty printing
    """
    test_cases = [["Simon says add 4", "Simon says add 6", "Then add 5"], ["Susan says add 10", "Simon says add 3", "Simon says multiply by 8"], ["Firstly, add 4", "Simeon says subtract 100"]]
    answers = [10, 24, 0]

    for i in range(len(test_cases)):
        assert simon_says(test_cases[i]) == answers[i]
        n = "\n"
        print(f"""simon_says([{n.join(test_cases[i])}])
output = {simon_says(test_cases[i])}\n""")

if __name__ == "__main__":
    main()