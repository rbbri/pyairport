from weather import Weather

class Airport():

    def __init__(self):
        self.hangar = []
        self.weather = Weather()

    def land(self, plane):
        self.__weatherCheck('Land')
        plane.land()
        self.__add(plane)
        return f"{plane} landed!"

    def take_off(self, plane):
        self.__weatherCheck('Take Off')
        plane.fly()
        self.__remove(plane)
        return f"{plane} airborne!"

    def __remove(self, plane):
        self.hangar.remove(plane)

    def __add(self, plane):
        self.hangar.append(plane)

    def __weatherCheck(self, process):
        if self.weather.isStormy():
            raise Exception(f'{process} aborted!')
