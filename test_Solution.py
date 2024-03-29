from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution: Solution = Solution('penztar.txt')

    def test_first_exercise(self):
        self.assertEqual(self.solution.num_of_payments, 141)

    def test_third_exercise(self):
        self.assertEqual(self.solution.items_bought(1), 1)
        self.assertEqual(self.solution.items_bought(2), 8)
        self.assertEqual(self.solution.items_bought(5), 5)
        self.assertEqual(self.solution.items_bought(7), 2)
        self.assertEqual(self.solution.items_bought(11), 1)

    def test_fifth_exercise(self):
        self.assertEqual(self.solution.min_was_bought("toll"), 1)
        self.assertEqual(self.solution.min_was_bought("kefe"), 5)
        self.assertEqual(self.solution.min_was_bought("szatyor"), 2)
        self.assertEqual(self.solution.min_was_bought("filctoll"), 4)
        self.assertEqual(self.solution.min_was_bought("ceruzaelem"), 1)
        self.assertEqual(self.solution.max_was_bought("toll"), 136)
        self.assertEqual(self.solution.max_was_bought("kefe"), 139)
        self.assertEqual(self.solution.max_was_bought("szatyor"), 138)
        self.assertEqual(self.solution.max_was_bought("filctoll"), 131)
        self.assertEqual(self.solution.max_was_bought("ceruzaelem"), 141)
        self.assertEqual(self.solution.total_was_bought("toll"), 35)
        self.assertEqual(self.solution.total_was_bought("kefe"), 32)
        self.assertEqual(self.solution.total_was_bought("szatyor"), 34)
        self.assertEqual(self.solution.total_was_bought("filctoll"), 29)
        self.assertEqual(self.solution.total_was_bought("ceruzaelem"), 31)

    def test_sixth_exercise(self):
        self.assertEqual(self.solution.money_needed(1), 500)
        self.assertEqual(self.solution.money_needed(2), 950)
        self.assertEqual(self.solution.money_needed(5), 2150)
        self.assertEqual(self.solution.money_needed(7), 2950)
        self.assertEqual(self.solution.money_needed(11), 4550)

    def test_seventh_exercise(self):
        self.assertEqual(self.solution.print_twb(2), None)
