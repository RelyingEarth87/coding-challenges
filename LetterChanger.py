def move(phrase: str) -> str:
    """A function to change the letters in a given phrase to the next letter in the alphabet

    Args:
        phrase (str): A string thats letters will be changed

    Returns:
        str: The changed string whose letters are offset by one letter from the original phrase
    """
    # making sure the phrase is all lowercase
    phrase = phrase.lower()

    # getting a list of all the ascii lowercase characters
    import string
    letters = string.ascii_lowercase

    # creating a cache of used letters for speed and ease
    # making z return a so it works for any character
    cache = {"z": "a"}
    # the new phrase to be returned
    new_phrase = ''
    for i in range(len(phrase)):
        # if a character in the string has already been converted, grabbing from cache
        if phrase[i] in cache.keys():
            new_phrase += cache[phrase[i]]
        # if not converted, finding the index from the reference string and getting the next one, the adding to string and cache
        else:
            letter_index = letters.find(phrase[i])
            cache[phrase[i]] = letters[letter_index + 1]
            new_phrase += letters[letter_index + 1]

    return new_phrase

def main():
    """Main entry point to do all the test cases
    """
    print(move("hello"))
    print(move("bye"))
    print(move("welcome"))
    print(move("zoo"))

if __name__ == "__main__":
    main()