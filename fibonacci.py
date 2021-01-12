def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    n = int(input('write number: '))
    print(fibonacci(n))


if __name__ == "__main__":
    main()
