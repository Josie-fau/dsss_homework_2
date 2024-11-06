import unittest

from math_quiz import random_int, random_op, calculate


class TestMathGame(unittest.TestCase):
    """
    includes 3 different tests for the math quiz
    - test random integer function
    - test random operator function
    - test calculate function
    returns runtime and
    OK  if all tests are passed
    FAILED (failures = numberOfFailures)
    """


    def test_random_in_range(self):
        """
        Test if random numbers generated are within the specified range
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_op(self):
        """
        Test if the random operator is either +,- or *
        """
        operator = random_op()
        assert operator == '+' or '-' or '*', f"Expected {'+, - or *'}, got {operator}"

    def test_calculate(self):
        """
        Test if calculations are performed correctly
        """
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 4, '+', '8 + 4', 12),
            (7, 2, '*', '7 * 2', 14),
            (10, 2, '*', '10 * 2', 20),
            (5, 3, '-', '5 - 3', 2),
            (5, 5, '-', '5 - 5', 0),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate(num1, num2, operator)
            assert problem == expected_problem, f"Expected {expected_problem}, got {problem}" #is problem string returned correctly?
            assert answer == expected_answer, f"Expected {expected_answer}, got {answer}" #is answer calculated correctly?
            """
            if problem == expected_problem and answer == expected_answer:
            pass
            """


if __name__ == "__main__":
    unittest.main()
