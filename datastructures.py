import csv

from package import Package

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


def insert_packages(csvfile, hashtable):
    # Reads data from csv file. Creates package objects and inserts into hash table.
    with open(csvfile) as packages_file:
        csv_reader = csv.reader(packages_file, delimiter=',')
        for row in csv_reader:
            package = Package(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], "At Hub")
            hashtable.insert(package.id, package)

    return hashtable

def insert_addresses(csvfile):
    # Reads data from csv file. Creates list of addresses.
    addresses = []

    with open(csvfile) as distances_file:
        csv_reader = csv.reader(distances_file, delimiter=',')
        for row in csv_reader:
            addresses.append(row[0])

    return addresses

def insert_distances(csvfile):
    # Reads data from csv file. Takes distance table csv and creates 2D Array of distances.
    distances = []

    with open(csvfile) as distances_file:
        csv_reader = csv.reader(distances_file, delimiter=',')
        for row in csv_reader:
            row_distance = []
            for i in range(1, len(row)):
                row_distance.append(row[i])
            distances.append(row_distance)

    return distances