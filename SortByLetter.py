def sort_by_letter(arr: list[str]) -> list:
    """Takes a list of strings with digits and one letter, and sorts them by the letter

    Args:
        arr (list[str]): a list with strings of digits and one letter

    Returns:
        list[str]: a new list of the strings sorted by the alphabetical order of the letters in them
    """
    import string
    if len(arr) == 0: 
        return []
    alphabet = string.ascii_lowercase

    order = {}

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] in alphabet:
                order[alphabet.find(arr[i][j])] = arr[i]
    
    sorted_order = sorted(order)

    sorted_arr = []

    for i in range(len(sorted_order)):
        sorted_arr.append(order[sorted_order[i]])


    return sorted_arr


def main():
    """A main entry point to handle test cases and printing in a readable manner
    """
    inputs = [["932c", "832u32", "2344b"], ["99a", "78b", "c2345", "11d"], ["572z", "5y5", "304q2"], []]
    outputs = [["2344b", "932c", "832u32"], ["99a", "78b", "c2345", "11d"], ["304q2", "5y5", "572z"], []]

    input_ = sort_by_letter(["932c", "832u32", "2344b"])
    for i in range(len(inputs)):
        output = sort_by_letter(inputs[i])
        assert output == outputs[i]

        print(f"""sort_by_letter({inputs[i]})
output = {output} \n""")

if __name__ == "__main__":
    main()