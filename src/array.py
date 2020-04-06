class DynamicArray:
    def __init__(self, capacity=1):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * capacity

    def insert(self, index, value):
        # Check capacity
        if self.count >= self.capacity:
            # If not add more capacity
            self.resize()
        # Shift over every item after index to right by 1
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]
        # Add the new value to the index
        self.storage[index] = value
        self.count += 1

    def append(self, value):
        if self.count >= self.capacity:
            self.resize()
        self.storage[self.count] = value
        self.count += 1

    def resize(self):
        # double capacity
        self.capacity *= 2
        # Allocate a new storage array with double capacity
        new_storage = [None] * self.capacity
        # Copy elements
        for i in range(self.count):
            new_storage[i] = self.storage[i]
            self.storage = new_storage


a = DynamicArray(2)
a.insert(0, 10)
a.insert(0, 11)
print(a.storage)
a.append(9)
a.append(8)
print(a.storage)
a.append(7)
print(a.storage)
