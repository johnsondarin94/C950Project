# This is the Package Class. This handles creating a Package object, returning the package id and address id. The String
# function is also overloaded here to provide legible displaying of the package object.
class Package:
    # Initialize the Package object
    # Time Complexity: O(1)
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes, status, time_to_leave,
                 time_delivered, address_id):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.time_to_leave = time_to_leave
        self.time_delivered = time_delivered
        self.address_id = address_id

    # Return Package ID
    # Time Complexity: O(1)
    def get_package_id(self):
        return self.package_id

    # Return Address ID
    # Time Complexity: O(1)
    def get_address_id(self):
        return self.address_id

    # Overload String Function to better display Package Object
    # Time Complexity: O(1)
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.package_id, self.address, self.city, self.state, self.zip_code, self.deadline, self.weight, self.notes,
            self.status, self.time_to_leave, self.time_delivered, self.address_id)
