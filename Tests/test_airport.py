import unittest
import random
from unittest import mock
from pretend import stub
from Src.airport import Airport
from Src.plane import Plane
from IPython.core.debugger import Tracer


class airportTest(unittest.TestCase):

    def setUp(self):
            self.airport = Airport()
            self.planes = self.airport.hangar
            self.plane = mock.Mock()
            self.fine_weather = stub(isStormy=lambda: False)
            self.stormy_weather = stub(isStormy=lambda: True)

    def test_init(self):
            self.assertEqual(len(self.planes), 0)

    def test_land_message(self):
            self.airport.weather = self.fine_weather
            landing = self.airport.land(self.plane)
            message = f"{self.plane} landed!"
            self.assertEqual(message, landing)

    def test_land_add(self):
            self.airport.weather = self.fine_weather
            self.airport.land(self.plane)
            self.assertEqual(self.planes, [self.plane])

    def test_land_warning(self):
            self.airport.weather = self.stormy_weather
            self.assertRaises(Exception, lambda: self.airport.land(self.plane))

    def test_take_off_message(self):
            self.airport.weather = self.fine_weather
            self.airport.land(self.plane)
            take_off = self.airport.take_off(self.plane)
            message = f"{self.plane} airborne!"
            self.assertEqual(message, take_off)

    def test_take_off_remove(self):
            self.airport.weather = self.fine_weather
            self.airport.land(self.plane)
            self.airport.take_off(self.plane)
            self.assertEqual(self.planes, [])

    def test_take_off_warning(self):
            self.airport.land(self.plane)
            self.airport.weather = self.stormy_weather
            self.assertRaises(Exception, lambda: self.airport.take_off(self.plane))



if __name__ == '__main__':
    unittest.main()
