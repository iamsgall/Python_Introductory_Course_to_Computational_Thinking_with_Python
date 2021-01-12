# assert <expression boolean>, <error message>


def firstLetter(listWords):
    letters = []

    for word in listWords:
        try:
            assert type(word) == str, f'{word} is not str'
            assert len(word) > 0, f'empty strings are not allowed'

            letters.append(word[0])
        except AssertionError as e:
            print(e)

    return letters


def main():
    print(firstLetter([1, 'katy']))


if __name__ == "__main__":
    main()
