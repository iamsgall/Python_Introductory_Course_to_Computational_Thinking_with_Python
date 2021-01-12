def splitElementsList(listNum, divider):
    try:
        return [i / divider for i in listNum]
    except ZeroDivisionError as e:
        print(e)
        return listNum


def main():
    listNum = list(range(10))
    divider = 0
    print(splitElementsList(listNum, divider))


if __name__ == "__main__":
    main()
