def pingPong(arr: list[str], results: bool) -> list[str]:
    """Given a list of "Pings" representing the serving player in a Ping Pong match, returns a list of the sounds of the whole match

    Args:
        arr (list[str]): a list of "Ping!"s representing the noises a serving player makes when hitting a Ping Pong Ball
        results (bool): True if the last ball is returned by the 2nd player, False if server scores

    Returns:
        list[str]: A list of the sounds of a Ping Pong match ("Ping!" for serving player, "Pong!" for returning player)
    """
    game = []
    if results:
        for i in range(len(arr)):
            game.append("Ping!")
            game.append("Pong!")
    else:
        for i in range(len(arr) - 1):
            game.append("Ping!")
            game.append("Pong!")
        game.append("Ping!")

    return game

def main():
    """A main function to handle test cases and pretty printing the output
    """
    pings = [["Ping!"], ["Ping!", "Ping!"], ["Ping!", "Ping!", "Ping!"]]
    bools = [True, False, True]
    output = [["Ping!", "Pong!"], ["Ping!", "Pong!", "Ping!"], ["Ping!", "Pong!", "Ping!", "Pong!", "Ping!", "Pong!"]]

    for i in range(len(pings)):
        assert pingPong(pings[i], bools[i]) == output[i]

        print(f"pingPong({pings[i]}, {bools[i]}) -> {pingPong(pings[i], bools[i])} \n")

if __name__ == "__main__":
    main()