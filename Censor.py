def censor(phrase: str) -> str:
    """Takes a string and returns the string with every word over 4 characters censored with *s

    Args:
        phrase (str): a phrase to censor

    Returns:
        str: the phrase, but with every word over 4 characters censored with *s
    """
    words = phrase.split()

    code = ""
    for i in words:
        if len(i) > 4:
            code += ("*" * len(i))
            code += " "
        else:
            code += i
            code += " "
    
    return code.strip()

def main():
    """Handles test cases and pretty printing
    """
    test_cases = ["The code is fourty", "Two plus three is five", "aaaa aaaaa 1234 12345"]
    answers = ["The code is ******", "Two plus ***** is five", "aaaa ***** 1234 *****"]

    for i in range(len(test_cases)):
        result = censor(test_cases[i])
        
        assert result == answers[i]

        print(f"""censor({test_cases[i]})
output = {result}\n""")

if __name__ == '__main__':
    main()