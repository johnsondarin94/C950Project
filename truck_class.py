# This is the Truck class. This handles creating the truck object, loading packages onto a truck, adding miles as the
# truck progresses, and returning a grand total miles traveled by instantiated truck.
class Truck:
    # Initializes the Truck object
    # Time Complexity: O(1)
    def __init__(self, loaded_package_ids, time_to_leave):
        self.loaded_package_ids = loaded_package_ids
        self.time_to_leave = time_to_leave
        self.loaded_packages = []
        self.miles_traveled = 0

    # Add packages to the loaded_packages list
    # Time Complexity: O(1)
    def load_package(self, package):
        self.loaded_packages.append(package)

    # Return the list of all packages
    # Time Complexity: O(1)
    def return_loaded_packages(self):
        return self.loaded_packages

    # Add miles traveled(float)
    # Time Complexity: O(1)
    def add_miles(self, count):
        self.miles_traveled += count

    # Return total miles traveled by truck(float)
    # Time Complexity: O(1)
    def return_miles_traveled(self):
        return self.miles_traveled

