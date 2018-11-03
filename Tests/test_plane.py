import unittest

from plane import Plane


class planeTest(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()

    def test_init(self):
        self.assertEqual(self.plane.airborne, False)

    def test_fly(self):
        self.plane.fly()
        self.assertEqual(self.plane.airborne, True)

    def test_land(self):
        self.plane.fly()
        self.plane.land()
        self.assertEqual(self.plane.airborne, False)
