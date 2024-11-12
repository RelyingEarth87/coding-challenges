def keyboardShortcut(con: str) -> str:
    """Takes a string with copy and paste shortcuts and returns the string with the words copied and pasted accordingly

    Args:
        con (str): the string of words and commands

    Returns:
        str: the words modified with the copy and paste actions
    """
    words: list = con.split()
    i = 0
    while i < len(words):
        if words[i] == "C":
            clip = words[0:i]
            temp = " ".join(clip)
            hold = temp.strip()
            words.remove(words[i])
            i -= 1
        elif words[i] == "V":
            try:
                words.remove(words[i])
                words.insert(i, hold)
                i -= 1
            except:
                words.remove(words[i])
                i -= 1
        elif words[i] in ["Ctrl", "+", "C", "V"]:
            words.remove(words[i])
            i -= 1
        i += 1

    end = " ".join(words)
    return end.strip()

def main():
    """A main function for handling the test cases and pretty printing
    """
    test_cases = ["the egg and Ctrl + C Ctrl + V the spoon", "WARNING Ctrl + V Ctrl + C Ctrl + V", "The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V"]
    answers = ["the egg and the egg and the spoon", "WARNING WARNING", "The The Town The The Town"]
    for i in range(len(test_cases)):
        assert keyboardShortcut(test_cases[i]) == answers[i]
        print(f'keyboardShortcut({[test_cases[i]]}) -> "{answers[i]}"')

if __name__ == "__main__":
    main()