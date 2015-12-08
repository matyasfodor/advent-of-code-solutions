from unittest import TestCase

from task1 import solution


class TestDay_02_1(TestCase):

    def test_correct(self):

        self.assertEqual(solution(), 1598415)
