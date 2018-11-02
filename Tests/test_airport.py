import unittest
from unittest import mock

from airport import Airport
from plane import Plane


class airportTest(unittest.TestCase):

    def setUp(self):
            self.airport = Airport()
            self.planes = self.airport.planes
            self.plane = mock.Mock()

    def test_init(self):
            self.assertEqual(len(self.planes), 0)

    def test_land_message(self):
            landing = self.airport.land(self.plane)
            message = f"{self.plane} landed!"
            self.assertEqual(message, landing)

    def test_land_add(self):
            self.airport.land(self.plane)
            self.assertEqual(self.planes, [self.plane])

    def test_take_off_message(self):
            self.airport.land(self.plane)
            take_off = self.airport.take_off(self.plane)
            message = f"{self.plane} airborne!"
            self.assertEqual(message, take_off)

    def test_take_off_remove(self):
            self.airport.land(self.plane)
            self.airport.take_off(self.plane)
            self.assertEqual(self.planes, [])

if __name__ == '__main__':
    unittest.main()
