import unittest

from moveZero import zero

class TestMoveZero(unittest.TestCase):
    def test_zero(self):

        # test areas when radius >=0
        self.assertAlmostEqual(zero([0,5,0,6,0]), [0,0,0,5,6])
        self.assertAlmostEqual(zero([0,0,0,0,0]), [0,0,0,0,0])
        self.assertAlmostEqual(zero([5,6,7,0,0]), [0,0,5,6,7])