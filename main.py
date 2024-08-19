import csv
from pydoc import locate

from package import Package

class HashTable:
    def __init__(self, size = 20):
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

    def delete(self, id):
        index = hash(id) % self.size
        index_list = self.table[index]

        for package in index_list:
            if package[0] == id:
                index_list.remove(package)

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

def min_distance(address1, addressList):
    min = None
    min_address = None
    for i in range(0, len(addressList)):
        distance = find_distance(address1, addressList[i])
        if min is None or distance < min:
            min = distance
            min_address = addressList[i]
    print(min)
    print(min_address)


def change_status(id):
    package = package_hash.find(id)
    if package is None:
        print("Error! Package does not exist.")
    else:
        package.status = "On Truck"

package_hash = HashTable()
insert_packages('packages.csv')
address_list = insert_addresses('distancetable.csv')
distances_list = insert_distances('distancetable.csv')

min_distance(package_hash.find(3).address, address_list)

