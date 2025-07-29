def is_authentic_skewer(skewer: str) -> bool:
    """Takes a "skewer" of letters and verifies if it alternates correctly in consonant-vowel-consonant pairs and is evenly spaced

    Args:
        skewer (str): a "skewer" (like a meat skewer) of uppercase letter characters and - (representing the stick) 

    Returns:
        bool: True if all criteria of a valid, well-made skewer exist; False otherwise
    """
    import re
    all_ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        if skewer[0] not in (all_ + "-") or skewer[1] not in (all_ + "-"):
            return False
    except IndexError:
        return False

    dashes = [x for x in re.split(rf"[{all_}]", skewer) if x != '']

    spacing = len(dashes[0])

    for i in dashes[1:]:
        if len(i) != spacing:
            return False
    

    vowels = ["A", "E", "I", "O", "U"]

    letters = [x for x in skewer.split("-") if x != ""]
    
    if letters[0] in vowels:
        return False
    else:
        curr = 1
        start = 1

    for i in letters[1:]:
        if curr == 0 and i in vowels:
            return False
        elif curr == 1 and i not in vowels:
            return False
        else:
            curr += 1
            curr = curr % 2
    
    return True


def main():
    test_cases = ["B--A--N--A--N--A--S", "A--X--E", "C-L-A-P", "M--A---T-E-S", ""]
    answers = [True, False, False, False, False]

    for i in range(len(test_cases)):
        result = is_authentic_skewer(test_cases[i])

        assert result == answers[i]

        print(f"""is_authentic_skewer("{test_cases[i]}")
output = {result}\n""")

if __name__ == "__main__":
    main()