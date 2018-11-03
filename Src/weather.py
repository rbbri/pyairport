import random

class Weather():

    def isStormy(self):
        if self.randomChoice() < 0.1:
            return True

    def randomChoice(self):
        return random.random()
