from unittest import TestCase

from .task1 import solution


class TestDay_01_1(TestCase):

    def test_correct(self):

        self.assertEqual(solution(), 280)
