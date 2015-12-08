from unittest import TestCase

from .task2 import solution


class TestDay_01_2(TestCase):

    def test_correct(self):

        self.assertEqual(solution(), 1797)
