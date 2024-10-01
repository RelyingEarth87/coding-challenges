import sys
import re
import os

def bytes_num(filepath: str) -> int:
    """Returns the number of bytes in a given file

    Args:
        filepath (str): the path to/name of the file

    Returns:
        int: number of bytes in the given file
    """
    return os.stat(filepath).st_size

def file_lines(filepath: str) -> int:
    """Returns the number of lines in a given file

    Args:
        filepath (str): the path to/name of the file

    Returns:
        int: number of lines in the given file
    """
    with open(filepath, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        return len(lines)

def num_words(filepath: str) -> int:
    """Returns the number of words in a given file

    Args:
        filepath (str): the path to/name of the file

    Returns:
        int: number of words in the given file
    """
    with open(filepath, 'r', encoding='UTF-8') as f:
        text = f.read()
        words = text.split(' ')
        return len(words)

def num_chars(filepath: str) -> int:
    """Returns the number of characters in a given file

    Args:
        filepath (str): the path to/name of the file

    Returns:
        int: number of characters in the given file
    """
    with open(filepath, 'r', encoding='UTF-8') as f:
        text = f.read()
        return len(text)

def main():
    """Main entry point to handle the arguments and options as well as output
    """
    args = ''.join(i + ' ' for i in sys.argv[1:])
    try:
        opts = re.search(r'\A-[clwmCLWM]', args).group()
    except AttributeError:
        opts = 'clw'
    try:
        filepath = re.search(r'[a-zA-Z]+[.][a-zA-Z]+', args).group()
    except AttributeError:
        filepath = "test.txt"

    output = []
    if 'c' in opts.lower():
        bytes = bytes_num(filepath)
        output.append(bytes)
    if 'l' in opts.lower():
        lines = file_lines(filepath)
        output.append(lines)
    if 'w' in opts.lower():
        words = num_words(filepath)
        output.append(words)
    if 'm' in opts.lower():
        chars = num_chars(filepath)
        output.append(chars)

    output.append(filepath)

    print(*output, sep=" ")


if __name__ == '__main__':
    main()
