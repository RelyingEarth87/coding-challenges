def convertTime(start: str) -> str:
    """Converts a time string from 12 hour to 24 hour time or vice versa
    Args:
        start (str): a time string either in 12 hour or 24 hour time format

    Returns:
        str: a time string opposite of the type of time string passed in
    """
    splt = start.split(":")
    if len(splt[1]) == 2:
        minutes = splt[1]
        startHour = int(splt[0])
        if startHour < 12:
            suffix = " am"
        else:
            suffix = " pm"
        if startHour in [12, 0, 24]:
            hours = 12
        else:
            hours = startHour % 12
    elif "am" in splt[1]:
        min_splt = splt[1].split(" ")
        minutes = min_splt[0]
        startHour = int(splt[0])
        if startHour == 12:
            hours = 0
        else:
            hours = startHour
        suffix = ""
    elif "pm" in splt[1]:
        min_splt = splt[1].split(" ")
        minutes = min_splt[0]
        startHour = int(splt[0])
        hours = (startHour + 12) % 24
        suffix = ""

    return str(hours) + ":" + minutes + suffix    


def main():
    """A main entry point to handle test cases and pretty printing
    """
    test_cases = ["12:00 am", "6:20 pm", "21:00", "5:05"]
    answers = ["0:00", "18:20", "9:00 pm", "5:05 am"]

    for i in range(len(test_cases)):
        result = convertTime(test_cases[i])
        assert result == answers[i]
        print(f"convertTime({test_cases[i]}) -> {result}")

if __name__ == "__main__":
    main()