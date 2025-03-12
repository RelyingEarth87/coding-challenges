def turnCalc(num: int) -> str:
    """Takes a series of numbers, converts them to their upside-down letter counterparts, and flips them backwards
    Like how you'd spell words on a calculator with upside-down numbers, this is "flipping the calculator around" to see what the word is

    Args:
        num (int): a series of numbers making up an upside down word

    Returns:
        str: the letters converted to a word after being "turned around"
    """
    table = {"1": "I", "2": "Z", "3": "E", "4": "H", "5": "S", "6": "G", "7": "L", "8": "B", "9": "-", "0": "O", ".": ""}

    string = str(num)

    flipped = ""
    for i in string:
        flipped += table[i]
    
    return flipped[::-1]

def main():
    """Handles test cases and pretty printing
    """
    # have to handle hello as a string so that it doesn't error out because of leading 0
    test_cases = [707, 5508, 3045, "07734"]
    answers = ["LOL", "BOSS", "SHOE", "HELLO"]

    for i in range(len(test_cases)):
        result = turnCalc(test_cases[i])
        
        assert result == answers[i]
        print(f"""turnCalc({test_cases[i]})
output = {result}\n""")

if __name__ == "__main__":
    main()