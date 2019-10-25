class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # check if the current is at the last index
        if self.current == self.capacity:
            # reset current to the first index
            self.current = 0
        # add the new item to the current index
        self.storage[self.current] = item
        # increment the current count by 1
        self.current += 1

    def get(self):
        # return a list comprehension removing all None elements in list
        # return an item if the item is not None
        return [item for item in self.storage if item]
