
class Truck:
    def __init__(self, time, location):
        self.time = time
        self.time_left_hub = time
        self.location = location
        self.packages = []
        self.distance_traveled = 0.0

    def add_packages(self, unloaded_packages):
        for package in unloaded_packages:
            self.packages.append(package)
