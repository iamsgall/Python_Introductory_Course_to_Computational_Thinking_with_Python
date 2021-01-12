import math


def main():
    number = int(input('write number: '))
    if math.sqrt(number) % 1 == 0:
        print('square root')
    else:
        print('no square root')


if __name__ == "__main__":
    main()
