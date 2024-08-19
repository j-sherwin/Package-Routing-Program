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

def load_packages(csvfile):
    # Reads data from csv file. Creates package objects and inserts into hash table.
    with open(csvfile) as packages_file:
        csv_reader = csv.reader(packages_file, delimiter=',')
        for row in csv_reader:
            package = Package(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], "At Hub")
            package_hash.insert(package.id, package)

def change_status(id):
    package = package_hash.find(id)
    if package is None:
        print("Error! Package does not exist.")
    else:
        package.status = "On Truck"

package_hash = HashTable()
load_packages('packages.csv')
print(package_hash.table)
change_status(222)
print(package_hash.find(20))



