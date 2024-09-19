def changeEnough(change: list, tot: float) -> bool:
    """Given a list of the amount of each type of US coin and a total due, tells whether or not user can afford the item(s)

    Args:
        change (list): a list of the amount of each type of US coin in pocket
        tot (float): the total amount of a purchase

    Returns:
        bool: True if item can be afforded, False otherwise
    """
    quarters = change[0]
    dimes = change[1]
    nickels = change[2]
    pennies = change[3]

    pocket: float = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)

    if pocket >= tot:
        return True
    
    return False

def main():
    """Main entry point into the function to allow for handling of test cases and functional printing
    """
    changes = [[2, 100, 0, 0], [0, 0, 20, 5], [30, 40, 20, 5], [10, 0, 0, 50], [1, 0, 5, 219]]
    totals = [14.11, 0.75, 12.55, 3.85, 19.99]
    answers = [False, True, True, False, False]

    for i in range(len(changes)):
        assert changeEnough(changes[i], totals[i]) == answers[i]

        print(f"changeEnough({changes[i]}, {totals[i]}) -> {changeEnough(changes[i], totals[i])}\n")

if __name__ == "__main__":
    main()