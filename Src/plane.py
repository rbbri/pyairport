class Plane():

    def __init__(self):
        self.airborne = False

    def fly(self):
        self.airborne = True

    def land(self):
        self.airborne = False
