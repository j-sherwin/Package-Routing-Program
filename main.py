# Jonathan Sherwin - C950 - Student ID: 011064274
from contextlib import nullcontext
from datetime import timedelta
from datastructures import *
from truck import *

# Setting variables for color text output
cyan = "\033[36m"
magenta = "\033[35m"
red = '\033[31m'
blue = "\033[34m"
default = '\033[0m'

# Reads address and distances from csv and creates a list of addresses and a list of distances.
address_list = insert_addresses('distancetable.csv')
distances_list = insert_distances('distancetable.csv')

#Initializes hash table
package_hash = HashTable()

# Checks 2D Array of Distances to find distance between two addresses.
def find_distance(address1, address2):
    return distances_list[address_list.index(address1)][address_list.index(address2)]

# Uses greedy algorithm to determine the closest address from the list of remaining truck packages. Returns that address, distance, and package ID.
def min_distance(address1, truck_packages):
    short_distance = None
    min_address = None
    package_id = None
    for i in range(0, len(truck_packages)):
        truck_package_address = package_hash.find(truck_packages[i]).address
        distance = float(find_distance(address1, truck_package_address))
        if short_distance is None or distance < short_distance:
            short_distance = distance
            min_address = truck_package_address
            package_id = truck_packages[i]
    return [min_address, package_id, short_distance]

def deliver_packages(truck, selected_time):
    # If time truck leaves hub is later than the user inputted time, no packages will be delivered.
    if truck.time_left_hub > selected_time:
        return True
    # Package 9 updates to correct address at 10:20
    if truck.time >= timedelta(hours=10, minutes=20):
        package_hash.find(9).address = "410 S State St"
    # Begins to deliver packages. Loops through packages on truck and runs min_distance function to determine where to deliver next.
    for package in truck.packages:
        package_hash.find(package).status = "En Route"
        if truck.time_left_hub == timedelta(hours=8):
            package_hash.find(package).truck = "Truck 1"
        elif truck.time_left_hub == timedelta(hours=10, minutes=20):
            package_hash.find(package).truck = "Truck 2"
        else:
            package_hash.find(package).truck = "Truck 3"
    while len(truck.packages) > 0:
        address, package_id, distance = min_distance(truck.location, truck.packages)
        delivery_time = timedelta(hours = distance / 18)
        truck.time += delivery_time
        # If truck's time becomes greater than user inputted time, function exits and status of all packages will be preserved in hash table for printing.
        if truck.time > selected_time:
            return True
        truck.distance_traveled += distance
        truck.location = address
        truck.packages.remove(package_id)
        package_hash.find(package_id).status = f"Delivered at {truck.time}"

    # Checks if this is the first truck to leave the hub (truck1). Sends truck back to hub so driver can take truck2
    if truck.time_left_hub == timedelta(hours=8):
        distance = float(find_distance(truck.location, address_list[0]))
        delivery_time = timedelta(hours = distance / 18)
        truck.time += delivery_time
        truck.distance_traveled += distance
        truck.location = address_list[0]

def main():
    exit_menu = False

    while not exit_menu:
        # Inserts packages into hash
        insert_packages('packages.csv', package_hash)

        # Initializes three trucks with their time to leave the HUB and the HUB location.
        truck1 = Truck(timedelta(hours=8), address_list[0])
        truck2 = Truck(timedelta(hours=10, minutes=20), address_list[0])
        truck3 = Truck(timedelta(hours=9, minutes=5), address_list[0])

        # Packages are loaded onto each truck by their package ID
        truck1.add_packages([14, 15, 19, 16, 13, 20, 21, 1, 39, 10, 37, 34, 30])
        truck2.add_packages([18, 3, 36, 9, 27, 35, 2, 33, 28, 5, 24, 19, 38])
        truck3.add_packages([29, 7, 6, 17, 31, 32, 12, 8, 25, 26, 11, 23, 22, 40, 4])

        print(f"{blue}###############################################")
        print("########  WGUPS DELIVERY SYSTEM MENU  #########")
        print(f"###############################################{default}")
        print("Please Enter a Number to Select a Menu Option:")
        print("1. Show All Package Statuses at Specific Time")
        print("2. Show Single Package Status at Specific Time")
        print("3. Deliver All Packages and Show Mileage and Package Status")
        print("4. QUIT")
        selection = input("Enter Selection: ")
        match selection:
            case "1":
                # User inputs specific time, program outputs status of all packages at that time.
                try:
                    selected_time = input("Please Enter 24hr Time (HH:MM): ")
                    h, m = selected_time.split(":")
                    time = timedelta(hours=float(h),minutes=float(m))
                    deliver_packages(truck1, time)
                    deliver_packages(truck2, time)
                    deliver_packages(truck3, time)
                    print(f"\n{cyan}ID | Address | City | State | Zipcode | Deadline | Weight | Status | Truck{default}")
                    package_hash.print()
                    total_miles = truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled
                    print(f"\nTruck 1 Mileage: {truck1.distance_traveled:.2f}")
                    print(f"Truck 2 Mileage: {truck2.distance_traveled:.2f}")
                    print(f"Truck 3 Mileage: {truck3.distance_traveled:.2f}")
                    print(f"\n{red}Total Mileage Traveled by All Trucks at {time}: {total_miles:.2f} miles\n{default}")
                except ValueError:
                    print("Invalid Input - Returning to Main Menu")
            case "2":
                # User inputs specific time and specific package ID. Program outputs that package's status
                try:
                    selected_time = input("Please Enter 24hr Time (HH:MM): ")
                    h, m = selected_time.split(":")
                    time = timedelta(hours=float(h),minutes=float(m))
                    selected_package = input("Please Enter a Package ID (1-40): ")
                    deliver_packages(truck1, time)
                    deliver_packages(truck2, time)
                    deliver_packages(truck3, time)
                    print(f"\n{cyan}ID | Address | City | State | Zipcode | Deadline | Weight | Status{default}")
                    print(package_hash.find(int(selected_package)))
                    total_miles = truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled
                    print(f"\nTruck 1 Mileage: {truck1.distance_traveled:.2f}")
                    print(f"Truck 2 Mileage: {truck2.distance_traveled:.2f}")
                    print(f"Truck 3 Mileage: {truck3.distance_traveled:.2f}")
                    print(f"\n{red}Total Mileage Traveled by All Trucks at {time}: {total_miles:.2f} miles\n{default}")
                except ValueError:
                    print("Invalid Input - Returning to Main Menu")
            case "3":
                # All packages are delivered. All relevant delivery stats are displayed.
                time = timedelta(days=1)
                deliver_packages(truck1, time)
                deliver_packages(truck2, time)
                deliver_packages(truck3, time)
                print(f"\n{cyan}ID | Address | City | State | Zipcode | Deadline | Weight | Status{default}")
                package_hash.print()
                total_miles = truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled
                print(f"\n{red}Total Mileage Traveled by All Trucks: {total_miles:.2f} miles\n{default}")
                print("Truck 1\n_______________________________")
                print(f"Left Hub: {truck1.time_left_hub}\nFinished Delivering: {truck1.time}\nFinal Location: {truck1.location}\nTotal Mileage: {truck1.distance_traveled:.2f}")
                print("\nTruck 2\n_______________________________")
                print(f"Left Hub: {truck2.time_left_hub}\nFinished Delivering: {truck2.time}\nFinal Location: {truck2.location}\nTotal Mileage: {truck2.distance_traveled:.2f}")
                print("\nTruck 3\n_______________________________")
                print(f"Left Hub: {truck3.time_left_hub}\nFinished Delivering: {truck3.time}\nFinal Location: {truck3.location}\nTotal Mileage: {truck3.distance_traveled:.2f}\n")
            case "4":
                # Exits Program
                exit_menu = True
            case _:
                print("Invalid Input - Please Try Again")

if __name__ == '__main__':
    main()