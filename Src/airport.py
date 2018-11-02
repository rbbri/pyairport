class Airport():

    def __init__(self):
        self.planes = []

    def land(self, plane):
        self.planes.append(plane)
        return f'{plane} landed!'

    def take_off(self, plane):
        return f"{plane} airborne!"
