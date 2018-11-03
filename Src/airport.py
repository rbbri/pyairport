from weather import Weather

class Airport():

    def __init__(self):
        self.hangar = []
        self.weather = Weather()

    def land(self, plane):
        if self.weather.isStormy():
            raise Exception('Landing aborted!')
        plane.land()
        self.__add(plane)
        return f"{plane} landed!"

    def take_off(self, plane):
        if self.weather.isStormy():
            raise Exception('Take Off aborted!')
        plane.fly()
        self.__remove(plane)
        return f"{plane} airborne!"

    def __remove(self, plane):
        self.hangar.remove(plane)

    def __add(self, plane):
        self.hangar.append(plane)
