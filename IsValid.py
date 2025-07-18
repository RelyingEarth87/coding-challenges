def isValid(sequence: str) -> str:
    """Determines if a string of characters either has the same number of frequencies for all letters, or if removing one character will make it valid

    Args:
        sequence (str): a string of letters

    Returns:
        str: "YES" if string is valid or can be made valid with 1 character removal, "NO" otherwise
    """
    freq = {}

    for i in sequence:
        if i not in freq.keys():
            num = sequence.count(i)
            freq[i] = num
    
    vals = list(freq.values())

    if max(vals) == min(vals):
        return "YES"
    elif max(vals) == min(vals) + 1 and vals.count(max(vals)) == 1:
        return "YES"
    elif min(vals) == 1 and vals.count(min(vals)) == 1:
        return "YES"
    else:
        return "NO"

def main():
    test_cases = ["abc", "abcc", "abccc", "aabbcd", "aabbccddeefghi", "abcdefghhgfedecba", "aabbccd"]
    answers = ["YES", "YES", "NO", "NO", "NO", "YES", "YES"]

    for i in range(len(test_cases)):
        result = isValid(test_cases[i])

        assert result == answers[i]

        print(f"""isValid("{test_cases[i]}")
output = "{result}"\n""")
        
if __name__ == "__main__":
    main()