class HashTable:
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * self.size
        self.used_slots = 0

    def hash_function(self, key):
        # A simple hash function that uses the ASCII values of the characters in the key
        hash_value = sum(ord(char) for char in key) % self.size
        return hash_value

    def put(self, key, data):
        if self.used_slots == self.size:
            raise MemoryError("Hash table is full.")

        hash_value = self.hash_function(key)
        while self.slots[hash_value] is not None and self.slots[hash_value].key != key:
            # Linear probing to find an empty slot or the slot with the matching key
            hash_value = (hash_value + 1) % self.size

        if self.slots[hash_value] is None:
            # If the slot is empty, create a new HashItem and increment the used_slots counter
            self.slots[hash_value] = HashItem(key, data)
            self.used_slots += 1
        else:
            # If the slot already contains a HashItem with the same key, update its data
            self.slots[hash_value].data = data
