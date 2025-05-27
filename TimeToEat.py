def timeToEat(curr_time: str) -> list[int]:
    """Takes a string of a time ("hh:mm a.m.") and returns the amount of time remaining before the next set mealtime

    Args:
        curr_time (str): a time string "hh:mm a.m."

    Returns:
        list[int]: [hours, minutes] before the next fixed mealtime
    """
    meal_times = [7, 12, 19]

    splt = curr_time.split()

    time_splt = splt[0].split(":")
    hour = int(time_splt[0])
    minute = int(time_splt[1])

    if splt[1][0] == "p":
        hour += 12
        hour = hour % 24

    last = 0
    for i in meal_times:
        if hour < i:
            last = i
            break
    
    if last == 0:
        last = meal_times[0]

    hour_remaining = (last - hour) % 24
    min_remaining = (0 - minute) % 60
    if min_remaining != 0:
        hour_remaining -= 1

    return [hour_remaining, min_remaining]

def main():
    test_cases = ["2:00 p.m.", "5:50 a.m."]
    answers = [[5, 0], [1, 10]]

    for i in range(len(test_cases)):
        result = timeToEat(test_cases[i])

        assert result == answers[i]

        print(f"""timeToEat({test_cases[i]})
output = {result}\n""")

if __name__ == "__main__":
    main()