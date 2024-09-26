def minutesToSeconds(time: str) -> int:
    """Takes a string representing a time %mm:%ss and returns the number of seconds

    Args:
        time (str): a time string, represented as %mm:%ss

    Returns:
        int: the number of seconds equivalent to the given time
    """
    minutes = int(time.split(':')[0])
    seconds = int(time.split(':')[1])

    if seconds > 59:
        return -1

    return (minutes * 60) + seconds

def main():
    """A main entry point into the program that allows for the handling of test cases and pretty printing of the function
    """
    times = ["01:00", "13:56", "10:60", "121:49"]
    answers = [60, 836, -1, 7309]

    for i in range(len(times)):
        assert minutesToSeconds(times[i]) == answers[i]
        print(f"minutesToSeconds({times[i]}) -> {minutesToSeconds(times[i])} \n")

if __name__ == "__main__":
    main()
