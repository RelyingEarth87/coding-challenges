def actualMemorySize(ms: str) -> str:
    """Takes a listed memory size for a device and returns the actual memory size

    Args:
        ms (str): the memory size of a device in ##GB or ##MB format

    Returns:
        str: the actual memory size of the device, rounded to the nearest MB or 10MB (for GB formats)
    """
    size = int(ms[:-2])
    label = ms[-2:]

    actual_size = size * .93

    output = ""
    if actual_size < 1 and label == "GB":
        output = f"{actual_size*1000: .0f}MB"
    elif label == "MB":
        output = f"{actual_size: .0f}{label}"
    else:
        output = f"{actual_size: .2f}{label}"

    return output.strip()

def main():
    test_cases = ["32GB", "2GB", "512MB"]
    answers = ["29.76GB", "1.86GB", "476MB"]

    for i in range(len(test_cases)):
        result = actualMemorySize(test_cases[i])

        assert result == answers[i]

        print(f"""actualMemorySize("{test_cases[i]}")
output = "{result}"\n""")

if __name__ == "__main__":
    main()