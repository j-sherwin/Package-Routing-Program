import csv
from datetime import time, timedelta, datetime

from package import Package
from truck import Truck


class HashTable:
    def __init__(self, size = 50):
        self.size = size
        self.table = []
        for i in range(self.size):
            self.table.append([])

    def insert(self, id, package):
        index = hash(id) % self.size
        index_list = self.table[index]

        for packages in index_list:
            if packages[0] == id:
                packages[1] = package
                return True

        index_list.append([id,package])
        return True

    def find(self, id):
        index = hash(id) % self.size
        if self.table[index] is not None:
            for package in self.table[index]:
                if package[0] == id:
                    return package[1]
        return None

    def print(self):
        for index, packages in enumerate(self.table):
            if packages:
                for id, package in packages:
                    print(package)

def insert_packages(csvfile):
    # Reads data from csv file. Creates package objects and inserts into hash table.
    with open(csvfile) as packages_file:
        csv_reader = csv.reader(packages_file, delimiter=',')
        for row in csv_reader:
            package = Package(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], "At Hub")
            package_hash.insert(package.id, package)

def insert_addresses(csvfile):
    addresses = []
    with open(csvfile) as distances_file:
        csv_reader = csv.reader(distances_file, delimiter=',')
        for row in csv_reader:
            addresses.append(row[0])
    return addresses

def insert_distances(csvfile):
    distances = []
    with open(csvfile) as distances_file:
        csv_reader = csv.reader(distances_file, delimiter=',')
        for row in csv_reader:
            row_distance = []
            for i in range(1, len(row)):
                row_distance.append(row[i])
            distances.append(row_distance)

    return distances

def find_distance(address1, address2):
    return distances_list[address_list.index(address1)][address_list.index(address2)]

def min_distance(address1, truck_packages):
    min = None
    min_address = None
    package_id = None
    for i in range(0, len(truck_packages)):
        truck_package_address = package_hash.find(truck_packages[i]).address
        distance = find_distance(address1, truck_package_address)
        if min is None or distance < min:
            min = distance
            min_address = truck_package_address
            package_id = truck_packages[i]
    return [min_address, package_id]

def deliver_packages(truck):

    for package in truck.packages:
        package_hash.find(package).status = "En Route"
    while len(truck.packages) > 0:
        next_stop = min_distance(truck.location, truck.packages)
        distance = float(find_distance(truck.location,next_stop[0]))
        delivery_time = timedelta(hours = distance / 18)
        truck.current_time += delivery_time
        truck.distance_traveled += distance
        truck.location = next_stop[0]
        truck.packages.remove(next_stop[1])
        package_hash.find(next_stop[1]).status = f"Delivered at {truck.current_time}"

package_hash = HashTable()
insert_packages('packages.csv')
address_list = insert_addresses('distancetable.csv')
distances_list = insert_distances('distancetable.csv')
truck1 = Truck(datetime(2024,8,18,8,0), address_list[0])
truck2 = Truck(datetime(2024,8,18,9,0), address_list[0])
truck1.add_packages([1, 5, 8, 6, 40, 23, 9])
truck2.add_packages([4, 7, 12, 25, 39, 32, 2])
deliver_packages(truck1)
deliver_packages(truck2)
package_hash.print()
print(truck1.distance_traveled + truck2.distance_traveled)
print(truck1.packages)
print(truck1.current_time)
print(truck2.current_time)