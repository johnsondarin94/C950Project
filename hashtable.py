# This is the HashTable class.
class HashTable:

    # Initialize an empty list then put additional lists within the list to serve as buckets.
    # Time Complexity: O(n)
    def __init__(self, capacity=10):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # Hashes a key(int) to return a unique value that determines where to put the value(package) within our hash table
    # Time Complexity: O(1)
    def hash(self, key):
        hash_value = hash(key) % len(self.table)
        return hash_value

    # Hashes a key to determine where the key/value pair will go then inserts the pair into the table.
    # Time Complexity: O(1)
    def insert(self, key, item):
        bucket = self.hash(key)
        bucket_list = self.table[bucket]
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Hashes a key to determine where the key/value pair will go then searches for a matching key from within the
    # table and if it is found it will update the value(package) with provided information
    # Time Complexity: O(n)
    def update(self, key, package):
        bucket = self.hash(key)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = package
                return True

    # Takes in a key(int) and returns the associated value(package) if the key is found.
    # Time Complexity: O(n)
    def search(self, key):
        bucket = self.hash(key)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    # Takes in a key(int) and removes the key/value pair from the bucket_list if the key is found
    # Time Complexity: O(n)
    def remove(self, key):
        bucket = self.hash(key)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])



