def damage(damage: int, speed=1, time="second") -> int:
    """calculates damage done over time

    Args:
        damage (int): the amount of damage per hit
        speed (int, optional): the number of hits per second. Defaults to 1.
        time (str, optional): the length of time spent hitting continuously. Defaults to "second".

    Returns:
        int: the amount of damage done over the given interval of time
    """
    if damage < 0 or speed < 0:
        return "invalid"

    if time == "second":
        mult = 1
    elif time == "minute":
        mult = 60
    elif time == "hour":
        mult = 60 * 60
    elif time == "day":
        mult = 60 * 60 * 24
    elif time == "week":
        mult = 60 * 60 * 24 * 7
    elif time == "month":
        mult = 60 * 60 * 24 * 30
    elif time == "year":
        mult = 60 * 60 * 24 * 365
    
    return damage * speed * mult

def main() -> None:
    """Main entry point, performs test cases
    """
    print(damage(40, 5, "second"))
    print(damage(100, 1, "minute"))
    print(damage(2, 100, "hour"))
    print(damage(-2, 100, "day"))
    print(damage(60, -4, "month"))

if __name__ == "__main__":
    main()