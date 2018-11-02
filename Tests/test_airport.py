import unittest
from unittest import mock

from airport import Airport
from plane import Plane


class airportTest(unittest.TestCase):

    def test_init(self):
            airport = Airport()
            planes = airport.planes
            self.assertEqual(len(planes), 0)

    def test_land_message(self):
            plane = mock.Mock()
            airport = Airport()
            landing = airport.land(plane)
            message = f"{plane} landed!"
            self.assertEqual(message, landing)

    def test_land_add(self):
            plane = mock.Mock()
            airport = Airport()
            landing = airport.land(plane)
            planes = airport.planes
            self.assertEqual(planes, [plane])

    def test_take_off_message(self):
            plane = mock.Mock()
            airport = Airport()
            take_off = airport.take_off(plane)
            message = f"{plane} airborne!"
            self.assertEqual(message, take_off)

if __name__ == '__main__':
    unittest.main()
