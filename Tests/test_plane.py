import unittest
from unittest import mock

from airport import Airport
from plane import Plane


class planeTest(unittest.TestCase):

    def test_init(self):
        plane = Plane()
        self.assertEqual(plane.airborne, False)

    def test_fly(self):
        plane = Plane()
        plane.fly()
        self.assertEqual(plane.airborne, True)

    def test_land(self):
        plane = Plane()
        plane.fly()
        plane.land()
        self.assertEqual(plane.airborne, False)
