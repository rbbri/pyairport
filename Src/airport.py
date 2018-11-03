class Airport():

    def __init__(self):
        self.planes = []

    def land(self, plane):
        plane.land()
        self.__add(plane)
        return f'{plane} landed!'

    def take_off(self, plane):
        plane.fly()
        self.__remove(plane)
        return f"{plane} airborne!"

    def __remove(self, plane):
        self.planes.remove(plane)

    def __add(self, plane):
        self.planes.append(plane)
