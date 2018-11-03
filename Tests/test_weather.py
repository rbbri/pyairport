import unittest
from pretend import stub
from weather import Weather

class weatherTest(unittest.TestCase):

# Testing stubbing in Python. These tests are irrelevant

    def test_state_stormy(self):
            stormy_weather = stub(isStormy=lambda: True)
            self.assertEqual(stormy_weather.isStormy(), True)
    def test_state_fine(self):
            fine_weather = stub(isStormy=lambda: False)
            self.assertEqual(fine_weather.isStormy(), False)
