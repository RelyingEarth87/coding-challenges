def loves_me(num: int) -> str:
    """Takes a number of petals and returns the classic game of loves me/loves me not

    Args:
        num (int): The number of petals on this pythonic flower

    Returns:
        str: A string representing loves me/loves me not based on the number of petals
    """
    options = ["loves me", "loves me not"]
    phrase = ""
    for i in range(num):
        current = options[i%len(options)]
        if i == num - 1:
            current = current.upper()
        elif i == 0:
            current =  current.capitalize()
        
        if phrase == "":
            phrase += current
        else:
            phrase = phrase + ', ' + current
    
    return phrase

def main():
    """A main entry point into the function allows for handling of test cases and pretty printing the results
    """
    test_cases = [3, 6, 1]
    answers = ["Loves me, loves me not, LOVES ME", "Loves me, loves me not, loves me, loves me not, loves me, LOVES ME NOT", "LOVES ME"]

    for i in range(len(test_cases)):
        assert loves_me(test_cases[i]) == answers[i]

        print(f"loves_me({test_cases[i]}) -> {loves_me(test_cases[i])} \n")

if __name__ == "__main__":
    main()