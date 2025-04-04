def spaceMessage(message: str) -> str:
    """Decrypts messages with code snippets in brackets that condense repeated characters

    Args:
        message (str): a message to be decoded

    Returns:
        str: the decrypted message
    """
    import re
    new = ""

    i = 0
    code = ""
    while i < len(message):
        if message[i] == "[":
            i += 1
            code += message[i]
        elif message[i] == "]":
            num = re.search(r"\d+", code).group()
            letters = re.search(r"[a-zA-z]+", code).group()
            code = ""
            new += letters * int(num)
        elif code != "":
            code += message[i]
        elif message[i].isalpha():
            new += message[i]
        else:
            print(message[i])

        i += 1
    
    return new

def main():
    """Runs a series of test cases to validate the spaceMessage function
    """
    test_cases = ["ABCD", "AB[3CD]", "IF[2E]LG[5O]D"]
    answers = ["ABCD","ABCDCDCD", "IFEELGOOOOOD"]

    for i in range(len(test_cases)):
        result = spaceMessage(test_cases[i])
        assert result == answers[i]

        print(f"""spaceMessage({test_cases[i]})
output = {result}\n""")

if __name__ == '__main__':
    main()