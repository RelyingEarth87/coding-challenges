#Did this first, it worked, realized it was technically wrong and redid it better
def simpleLemonade(purchases: list[int]) -> bool:
    """Determines if a vendor can make exact change from a number of lemonade stand purchases

    Args:
        purchases (list[int]): an ordered list of dollars spent per lemonade purchased

    Returns:
        bool: True if the vendor can make exact change; False otherwise
    """
    cost = 5
    change = 0
    for purchase in purchases:
        change_needed = (purchase - cost) / cost
        if change_needed > change:
            return False
        change -= change_needed
        change += 1
    
    return True

def lemonade(purchases: list[int]) -> bool:
    """Determines if a vendor can make exact change from a number of lemonade stand purchases

    Args:
        purchases (list[int]): an ordered list of bills spent per lemonade purchased

    Returns:
        bool: True if the vendor can make exact change; False otherwise
    """
    register = {"5": 0, "10": 0, "20": 0}

    for purchase in purchases:
        if purchase == 20:
            if register["10"] >= 1 and register["5"] >= 1:
                register["10"] -= 1
                register["5"] -= 1
            elif register["5"] >= 3:
                register["5"] -= 3
            else:
                return False
            register["20"] += 1

        elif purchase == 10:
            if register["5"] < 1:
                return False
            register["5"] -= 1
            register["10"] += 1

        elif purchase == 5:
            register["5"] += 1

    return True

def main():
    """
    Handles test cases and pretty printing"""
    test_cases = [[5, 5, 5, 10, 20], [5, 5, 10, 10, 20], [10, 10], [5, 5, 10]]
    answers = [True, False, False, True]

    for i in range(len(test_cases)):
        result1 = simpleLemonade(test_cases[i])
        result = lemonade(test_cases[i])
        
        assert result1 == answers[i]
        assert result == answers[i]

        print(f"""lemonade({test_cases[i]})
output = {result}\n""")

if __name__ == "__main__":
    main()