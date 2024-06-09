def fizzbuzz(n: int) -> list[str]:
    output: list = []
    for i in range(1, n + 1):
        current: str = ''
        if i % 3 == 0:
            current += 'Fizz'
        if i % 5 == 0:
            current += 'Buzz'
        if i % 5 != 0 and i % 3 != 0:
            current += str(i)
        output.append(current)
    
    return output

def main() -> None:
    print(fizzbuzz(3))
    print(fizzbuzz(5))
    print(fizzbuzz(15))


if __name__ == '__main__':
    main()
