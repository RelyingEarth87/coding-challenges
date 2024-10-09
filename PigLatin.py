def pigLatinSentence(sentence: str) -> str:
    """Converts a sentence from English into Pig Latin

    Args:
        sentence (str): a sentence or phrase in English

    Returns:
        str: A sentence or phrase in Pig Latin
    """
    import re
    vowels = ["a", "e", "i", "o", "u"]

    pigLatin = ""
    for word in sentence.split(" "):
        first = word[0]

        if first.lower() in vowels:
            pl = word + "way"
        else:
            pos = re.search(r"[aeiou]", word).start()
            pl = word[pos:] + word[:pos].lower() + "ay"
        
        pigLatin = pigLatin + " " + pl

    final = pigLatin.strip()
    return final

def main():
    """A main function to handle test cases and pretty printing
    """
    test_cases = ["this is pig latin", "wall street journal"]
    answers = ["isthay isway igpay atinlay", "allway eetstray ournaljay"]

    for i in range(len(test_cases)):
        assert pigLatinSentence(test_cases[i]) == answers[i]

        print(f"pigLatinSentence({test_cases[i]}) -> {pigLatinSentence(test_cases[i])} \n")

if __name__ == '__main__':
    main()