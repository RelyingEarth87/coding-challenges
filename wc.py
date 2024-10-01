import sys
import re
import os

def bytes_num(filepath):
    return os.stat(filepath).st_size

def file_lines(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        return len(lines)

def num_words(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        text = f.read()
        words = text.split(' ')
        return len(words)

def num_chars(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        text = f.read()
        return len(text)

def main():
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