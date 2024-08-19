from datetime import time


class Truck:
    def __init__(self, time_left, location):
        self.current_time = time_left
        self.time_left_hub = time_left
        self.location = location
        self.packages = []
        self.distance_traveled = 0.0

    def add_packages(self, unloaded_packages):
        for package in unloaded_packages:
            self.packages.append(package)
