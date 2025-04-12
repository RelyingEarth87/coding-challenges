def isLongPressed1(ideal: str, actual: str) -> bool:
    """Tells whether or not an entered word is the same as an expected one but with some accidental long key presses
    This version uses very bad logic and is not very efficient or elegant, but works

    Args:
        ideal (str): the expected word
        actual (str): the text entered by a user

    Returns:
        bool: True if word matches, potentially with extra of the same letters; False otherwise
    """
    # handling some cases separately
    import re

    diff_act = set(actual)

    for i in diff_act:
        if i not in ideal:
            return False
        num_idl = len(re.findall(i, ideal))
        num_act = len(re.findall(i, actual))
        if num_idl > num_act:
            return False

    ideal = [i for i in ideal]
    actual: list = [i for i in actual]

    length = len(actual)
    curr = 0
    first = True
    while len(actual) > 0:
        if first == True and actual[0] != ideal[0]:
            return False
        else:
            first = False

        if ideal[curr] == actual[0]:
            actual.pop(0)
        else:
            curr += 1

        if curr >= length:
            return False
    
    return True

def isLongPressed(ideal: str, actual: str) -> bool:
    """Tells whether or not an entered word is the same as an expected one but with some accidental long key presses

    Args:
        ideal (str): the expected word
        actual (str): the text entered by a user

    Returns:
        bool: True if word matches, potentially with extra of the same letters; False otherwise
    """
    # all regex
    import re

    search_str = r"^"
    for i in range(len(ideal)):
        if i == len(ideal)-1:
            search_str += f"{ideal[i]}*"
            search_str += f"{ideal[i]}$"
        else:
            search_str += f"{ideal[i]}+"

    match = re.search(search_str, actual)

    if match:
        return True
    else:
        return False

def main():
    """Handles test cases
    """
    test_cases = [("alex", "aaleex"), ("saeed", "ssaaedd"), ("leelee", "lleeelee"), ("Tokyo", "TTokkyoh"), ("laiden", "laiden")]
    answers = [True, False, True, False, True]

    for i in range(len(test_cases)):
        case_ = test_cases[i]
        result = isLongPressed(case_[0], case_[1])

        assert result == answers[i]

        print(f"""isLongPressed({case_[0]}, {case_[1]})
output = {result}\n""")

if __name__ == "__main__":
    main()