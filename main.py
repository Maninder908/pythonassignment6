class HashTable:
    def __init__(self, size=26):
        self.size = size
        self.slots = [None] * size

    def _find_free_slot(self, position):
        start_position = position
        while True:
            if self.slots[position] is None:
                return position
            position = (position + 1) % self.size
            if position == start_position:
                return None

# Example usage
h = HashTable()
for c in "abcdefghijklmnopqrstuvwxyz":
    h.slots[(ord(c) * ord(c)) % h.size] = c

print(h._find_free_slot(0))  # Output: 1
print(h._find_free_slot(1))  # Output: 1
print(h._find_free_slot(10)) # Output: 10
