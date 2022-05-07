import csv
from package_class import Package
from hashtable import HashTable

htable = HashTable()


# Reads in WGUPSPackageFile.csv, creates package objects with provided parsed data, and adds package to hashtable with
# provided package ID and package object as Key/Value pairs respectively.
# Time Complexity: O(n)
def load_package_file():
    address_data = load_address_data()
    with open('WGUPSPackageFile.csv', encoding='utf-8-sig') as package_file:
        package_data = csv.reader(package_file, delimiter=',')

        # Packages are given an associated address ID to better represent delivery destination for the computer
        for package in package_data:
            package_id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip_code = package[4]
            deadline = package[5]
            weight = package[6]
            notes = package[7]
            status = 'at the hub'
            time_to_leave = ''
            time_delivered = ''

            for location in address_data:
                if address == location[2].strip():
                    address_id = location[0]
                    break

            package = Package(package_id, address, city, state, zip_code, deadline, weight, notes, status,
                              time_to_leave, time_delivered, address_id)

            htable.insert(package_id, package)
    return htable


# Returns Hash Table
# Time Complexity: O(1)
def get_hash_table():
    return htable


# Reads in WGUPSDistanceTable.csv
def load_distance_data():
    with open('WGUPSDistanceTable.csv', encoding='utf-8-sig') as distance_file:
        distances = list(csv.reader(distance_file, delimiter=','))
        return distances


# Reads in WGUPSDistanceTableAddresses.csv
def load_address_data():
    with open('WGUPSDistanceTableAddresses.csv', encoding='utf-8-sig') as distance_file_addresses:
        addresses = list(csv.reader(distance_file_addresses, delimiter=','))
        return addresses
