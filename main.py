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

def find_distance(package1, package2):
    package1_index = 0
    package2_index = 0
    for i in range (0, len(address_list)):
        if address_list[i] == package1.address:
            package1_index = i
            break
    for i in range (0, len(address_list)):
        if address_list[i] == package2.address:
            package2_index = i
            break
    return distances_list[package1_index][package2_index]

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
print(package_hash.find(4))
print(package_hash.find(10))
print(find_distance(package_hash.find(4), package_hash.find(10)))

