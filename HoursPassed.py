def timeConversion(time: str) -> int:
    """converts a 12 hour time string (hours only) to an integer divisible by 24

    Args:
        time (str): a time string (hh:mm AM/PM)

    Returns:
        int: an integer divisible by 24 representing an hour in 24 hour time
    """
    splt = time.split()
    meridian = splt[1]
    hours = int(splt[0].split(":")[0])

    if meridian == "PM":
        hours += 12

    return hours

def hoursPassed(time1: str, time2: str) -> str:
    """Takes 2 12-hour time strings (hours only) and returns the number of hours passed between the two times

    Args:
        time1 (str): the first time string (hh:mm AM/PM)
        time2 (str): the second time string (hh:mm AM/PM)

    Returns:
        str: a string representing the number of hours passed
    """
    code1 = timeConversion(time1)
    code2 = timeConversion(time2)

    if code2 == code1:
        return "no time passed"
    elif code2 > code1:
        return f"{code2 - code1} hours"
    else:
        code2 += 24
        return f"{code2 - code1} hours"

def main() -> None:
    """Handles test cases and pretty printing

    Returns:
        None: prints results of test cases
    """
    #added extra test case for pm at night and then am the next morning
    test_cases = [("3:00 AM", "9:00 AM"), ("2:00 PM", "4:00 PM"), ("1:00 AM", "3:00 PM"), ("4:00 PM", "4:00 PM"), ("8:00 PM", "5:00 AM")]
    answers = ["6 hours", "2 hours", "14 hours", "no time passed", "9 hours"]

    for i in range(len(test_cases)):
        result = hoursPassed(*test_cases[i])
        assert result == answers[i]
        print(f"""hoursPassed({test_cases[i][0], test_cases[i][1]})
output = {result}\n""")

if __name__ == '__main__':
    main()