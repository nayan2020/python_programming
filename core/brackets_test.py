import unittest
from bucket_check import solution


class TestSolution(unittest.TestCase):

    def test_solution_case_1(self):
        self.assertEqual(solution(['(', '(']), False)

    def test_solution_case_2(self):
        self.assertEqual(solution(['(', ')']), True)

    def test_solution_case_3(self):
        self.assertEqual(solution([')', '(']), False)

    def test_solution_case_4(self):
        self.assertEqual(solution(['(', '(', ')', ')']), True)

    def test_solution_case_5(self):
        self.assertEqual(solution([')', ')']), False)

    def test_solution_case_6(self):
        self.assertEqual(solution(['(', '(', ')', '(', ')']), False)

    def test_solution_case_7(self):
        self.assertEqual(solution(['(', ')', '(']), False)

    def test_solution_case_8(self):
        self.assertEqual(solution(['(', ')', ')']), False)

    def test_solution_case_9(self):
        self.assertEqual(solution(['(', '(', ')', '(', ')', ')']), True)

    def test_solution_case_10(self):
        self.assertEqual(solution(['(', '(', ')', '(', ')', '(']), False)

    def test_solution_case_11(self):
        self.assertEqual(solution(['[', '{', ')', '(', '}', ']']), False)

    def test_solution_case_12(self):
        self.assertEqual(solution(['[', '{', '(', ')', '}', ']']), True)

    def test_solution_case_13(self):
        self.assertEqual(solution(['[', '{', '(', '}', ')', ']']), False)


if __name__ == '__main__':
    unittest.main()
