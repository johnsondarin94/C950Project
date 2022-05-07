import datetime
import csvreader
from truck_class import Truck
from datetime import timedelta
from package_class import Package


# ---------- Explaining the program -----------
#
# The following algorithm uses the Nearest Neighbor approach to determine the shortest distance between packages on a
# truck. Nearest Neighbor calculates which distance is closest at a given time. This algorithm while it can miss the
# shortest route is simple to implement and practical for the given problem.
#
# The structure of the algorithm is as follows:
#
# * sort_truck_packages function is called with provided list of packages.
# * sort_truck_packages calls min_distance_from and adds each returned package to a new ordered list.
# * sort_truck_packages after each returned package, sets the from_address to the returned package.address_id, removes
# the package from the original list. and calls min_distance_from until all packages have been gone through.
#
# * min_distance_from accepts a from address and a list of packages. Using the provided information the function
# compares each adjacent item by calling the distance_between function. When a new shortest distance has been found it
# sets the min_distance variable to the new value.
# * Once all values in the list have been gone through, the final for loop matches up the package with the min_distance
# and returns that package to sort_truck_packages where it is added to the ordered list.
#
# * distance_between is used by min_distance_from to return a distance between 2 address IDs
#
# The Time Complexity of the entire program as well as the algorithm is: O(n^2)
#
#
# ---------- Algorithm Pseudocode -----------
#
# Nearest Neighbor
# A[1...n] where n = length[A]
#
#   for i, x in length A[n] (where i is every package in A)
#       for y in A[n + 1] (package adjacent to x)
#           if min_distance == 0
#               min_distance = (sets minimum distance to first values distance)
#           if x < y and x < min_distance
#               min_distance = x
#           if y < x and y < min_distance
#                min_distance = y
#   for i, x in length A[n]
#        if x == min_distance: (Matches package with min_distance)
#            return x (Returns package where package distance == min_distance)
#


# Returns distance between 2 address IDs using distance table
# Time Complexity: O(1)


def distance_between(address_1, address_2):
    distance_list = csvreader.load_distance_data()
    distance = distance_list[address_1][address_2]
    if distance == '':
        distance = distance_list[address_2][address_1]
    return float(distance)


# Determines minimum distance between 2 addresses in a list of packages by calling distance_between function and
# comparing the 2 addresses in a list. Returns the nearest package
# Time Complexity: O(n^2)
def min_distance_from(from_address, truck_packages):
    min_distance = 0
    for count, package_1 in enumerate(truck_packages):
        for package_2 in truck_packages[count + 1:]:
            distance_1 = distance_between(int(from_address), int(package_1.address_id))
            distance_2 = distance_between(int(from_address), int(package_2.address_id))
            if min_distance == 0:
                min_distance = distance_between(int(from_address), int(package_1.address_id))
            if distance_1 < distance_2 and distance_1 < min_distance:
                min_distance = distance_1
            if distance_2 < distance_1 and distance_2 < min_distance:
                min_distance = distance_2
    for count, package in enumerate(truck_packages):
        if distance_between(int(from_address), int(truck_packages[count].address_id)) == min_distance:
            return package


# Sort packages on a truck by calling the min_distance_from function. Adds the package that is returned to a new
# sorted list, sets the from_address to the package.address_id and then removes that package from the truck_package list
# to ensure it doesn't get called again. Once all packages have been cycled through the new sorted list is returned.
# Time Complexity: O(n)
def sort_truck_packages(truck_packages):
    from_address = 0
    truck_sorted_list = []
    while len(truck_packages) > 0:
        # To ensure no errors the proceeding if statement adds the final package onto the truck instead of calling
        # the min_distance_from function.
        if len(truck_packages) < 2:
            truck_sorted_list.append(truck_packages[0])
            break
        package = min_distance_from(from_address, truck_packages)
        truck_sorted_list.append(package)
        from_address = package.address_id
        truck_packages.remove(package)
    return truck_sorted_list


# This function creates 3 truck objects, manually loads the trucks and calls the sort_truck_packages to have them
# sorted by shortest distance.
# Time Complexity: O(n)
def truck_load_packages():
    htable = csvreader.load_package_file()
    truck_1 = Truck([1, 37, 14, 5, 15, 16, 8, 20, 12, 17, 13, 22, 23, 29, 30, 34], timedelta(hours=8, minutes=00,
                                                                                             seconds=00))
    truck_2 = Truck([3, 6, 21, 4, 7, 40, 18, 10, 19, 25, 28, 32, 36, 24, 26, 31], timedelta(hours=9, minutes=5,
                                                                                            seconds=00))
    truck_3 = Truck([9, 33, 27, 35, 2, 38, 39, 11], timedelta(hours=11, minutes=00, seconds=00))

    for package_id in truck_1.loaded_package_ids:
        package = htable.search(package_id)
        package.time_to_leave = truck_1.time_to_leave
        truck_1.load_package(package)

    for package_id in truck_2.loaded_package_ids:
        package = htable.search(package_id)
        package.time_to_leave = truck_2.time_to_leave
        truck_2.load_package(package)

    for package_id in truck_3.loaded_package_ids:
        package = htable.search(package_id)
        package.time_to_leave = truck_3.time_to_leave
        truck_3.load_package(package)

    truck_1.loaded_packages = (sort_truck_packages(truck_1.return_loaded_packages()))
    truck_2.loaded_packages = (sort_truck_packages(truck_2.return_loaded_packages()))
    truck_3.loaded_packages = (sort_truck_packages(truck_3.return_loaded_packages()))
    # Because package 9 will have been fixed before 11:00 am package is fixed here.
    package = htable.search(9)
    package.address = '410 S State St.'
    package.city = 'Salt Lake City'
    package.state = 'UT'
    package.zip_code = '84111'
    package.address_id = 19
    truck_list = [truck_1, truck_2, truck_3]
    return truck_list


# This function handles delivering the packages, updating the hash table, adding miles, and accumulating time.
# Time Complexity: O(n^2)
def truck_deliver_packages(truck_list, hash_table):
    for count2, truck in enumerate(truck_list):
        truck_time = truck.time_to_leave
        truck_packages = truck.loaded_packages
        for package in truck_packages:
            hash_table.update(package.package_id, update_package_info(package, truck_time, 'en route'))
        for count, package in enumerate(truck_packages):
            if count == 0:
                distance = distance_between(0, int(truck_packages[count].address_id)) / 18
                time_to_deliver = datetime.timedelta(hours=distance)
                truck_time = truck_time + time_to_deliver
                truck.add_miles(distance_between(0, int(truck_packages[count].address_id)))
                hash_table.update(truck_packages[count].package_id,
                                  update_package_info(package, truck_time, 'delivered'))
                continue

            distance = distance_between(int(truck_packages[count - 1].address_id),
                                        int(truck_packages[count].address_id)) / 18
            time_to_deliver = datetime.timedelta(hours=distance)
            truck_time = truck_time + time_to_deliver
            truck.add_miles(distance_between(int(truck_packages[count - 1].address_id),
                                             int(truck_packages[count].address_id)))
            hash_table.update(truck_packages[count].package_id, update_package_info(package, truck_time, 'delivered'))
            last_package = hash_table.search(truck_packages[-1].package_id)

            if last_package.status == 'delivered':
                truck.add_miles(distance_between(0, int(truck_packages[-1].address_id)))
                truck_time = truck_time + time_to_deliver
    return truck_list


# Handles updating packages as needed
# Time Complexity: O(1)
def update_package_info(package, time_delivered, status):
    package_id = package.package_id
    address = package.address
    city = package.city
    state = package.state
    zip_code = package.zip_code
    deadline = package.deadline
    weight = package.weight
    notes = package.notes
    status = status
    time_to_leave = package.time_to_leave
    time_delivered = time_delivered
    address_id = package.address_id
    updated_package = Package(package_id, address, city, state, zip_code, deadline, weight, notes, status,
                              time_to_leave,
                              time_delivered, address_id)
    return updated_package


# Prints the Hash Table contents as well as tally all truck miles together.
# Time Complexity: O(n)
def print_packages_tally_truck_miles(truck_list):
    htable = csvreader.get_hash_table()
    for count in range(1, 41):
        print(htable.search(count))
    print("Truck 1 traveled: " + str(truck_list[0].return_miles_traveled()))
    print("Truck 2 traveled: " + str(truck_list[1].return_miles_traveled()))
    print("Truck 3 traveled: " + str(truck_list[2].return_miles_traveled()))
    total_miles = truck_list[0].return_miles_traveled() + truck_list[1].return_miles_traveled() + truck_list[
        2].return_miles_traveled()
    print("Total Miles Traveled: " + str(total_miles))
