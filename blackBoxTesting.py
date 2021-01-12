import unittest


def add(num1, num2):
    return num1 + num2


class blackBoxTesting(unittest.TestCase):

    def test_sum_two_positives(self):
        num1 = 1
        num2 = 2

        result = add(num1, num2)
        self.assertEqual(result, 3)

    def test_sum_two_negatives(self):
        num1 = -1
        num2 = -2

        result = add(num1, num2)
        self.assertEqual(result, -3)


if __name__ == "__main__":
    unittest.main()
