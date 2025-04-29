def split_into_buckets(phrase: str, limit: int) -> list[str]:
    """Takes a phrase and breaks it up based on a given character limit

    Args:
        phrase (str): given phrase
        limit (int): character limit

    Returns:
        list[str]: string broken up into smaller segments of complete words and spaces up to a certain character limit 
    """
    words = phrase.split(" ")

    buckets = []

    bucket = ""
    i = 0
    while len(bucket) <= limit and i <= len(words):
        if i == len(words):
            buckets.append(bucket.strip())
            break

        length = len(bucket) + len(words[i]) + 1
        if length <= limit:
            bucket = bucket + " " + words[i]
            bucket = bucket.strip()
            i += 1
        else:
            buckets.append(bucket.strip())
            bucket = ""
    
    return buckets

def main():
    test_cases = [("she sells sea shells by the sea", 10), ("the mouse jumped over the cheese", 7), ("fairy dust coated the air", 20), ("a b c d e", 2)]
    answers = [["she sells", "sea shells", "by the sea"], ["the", "mouse", "jumped", "over", "the", "cheese"], ["fairy dust coated", "the air"], ["a", "b", "c", "d", "e"]]

    for i in range(len(test_cases)):
        result = split_into_buckets(test_cases[i][0], test_cases[i][1])

        assert result == answers[i]
        print(f"""split_into_buckets({test_cases[i][0]}, {test_cases[i][1]})
output = {result}\n""")

if __name__ == "__main__":
    main()
