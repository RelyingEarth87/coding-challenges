def numToEng(num: int) -> str:
    """Takes a number between 0 and 999 (inclusive) and returns a string representation of that number

    Args:
        num (int): any number 0-999

    Returns:
        str: a string representation of a number between 0 and 999 (inclusive)
    """
    name = str(num)
    length = len(name)

    ones = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
    teens = {"10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "15": "fifteen", "18": "eighteen"}
    special_tens = {"20": "twen", "30": "thir", "40": "for", "50": "fif"}

    num_name = " "
    words = []
    if length > 1:
        if name[-2] == "1":
            try:
                word = teens[name[-2:]]
            except KeyError:
                word = ones[name[-1]] + "teen"
        elif name[-2] and str(int(name[-2]) * 10) in special_tens:
            word = special_tens[str(int(name[-2]) * 10)] + "ty "
        elif name[-2] == "0":
            word = ""
        else:
            word = ones[name[-2]] + "ty "
            
        if name[-1] != "0" and name[-2] != "1":
            word += ones[name[-1]]
    else:
        word = ones[name]
    words.append(word)

    if length == 3:
        hundreds = ones[name[0]] + " hundred"
        words.insert(0, hundreds)

    num_name = num_name.join(words)

    return num_name.strip()

def main():
    """A main function to handle test cases and pretty printing
    """
    test_cases = [0, 18, 126, 909]
    answers = ["zero", "eighteen", "one hundred twenty six", "nine hundred nine"]

    for i in range(len(test_cases)):
        assert numToEng(test_cases[i]) == answers[i], f"Test case {i+1} failed"

        print(f"numToEng({test_cases[i]}) -> {answers[i]}\n")


if __name__ == "__main__":
    main()