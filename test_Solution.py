from unittest import TestCase
from Solution import Solution

class TestSolution(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution: Solution = Solution('penztar.txt')
