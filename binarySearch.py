def main():
    target = int(input('write a number: '))
    epsilon = 0.001
    low = 0.0
    hight = max(1.0, target)
    result = (low + hight) / 2

    while abs(result**2 - target) >= epsilon:
        print(f'low={low}, hight={hight}, result={result}')
        # print(abs(result**2 - target), result)

        if result**2 < target:
            low = result
        else:
            hight = result

        result = (hight + low) / 2

    print(f'square root {target} is {result}')


if __name__ == "__main__":
    main()
