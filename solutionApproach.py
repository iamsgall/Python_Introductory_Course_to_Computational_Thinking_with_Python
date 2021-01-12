def main():
    target = int(input('write number: '))
    epsilon = 0.01
    step = epsilon**2
    result = 0.0

    while abs(result**2 - target) >= epsilon and result <= target:
        result += step
        print(abs(result**2 - target), result)

    if abs(result**2 - target) >= epsilon:
        print(f'no square root {target}')
    else:
        print(f'square root {target} => {result}')


if __name__ == "__main__":
    main()
