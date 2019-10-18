class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        # 3 -> 2 -> 1 -> None reverse None <- 3 <- 2 <- 1
        # define variable to hold the node on the initial head
        current_node = self.head
        # define the variable previous to hold the current node
        previous_node = None
        # loop through the list if its not None
        while current_node:
            # define variable to hold the next node of the current_node
            next_node = current_node.next_node
            # set the current_node next_node to the previous_node
            current_node.next_node = previous_node
            # update the previous_node to the current_node
            previous_node = current_node
            # update the current_node to the next_node
            current_node = next_node
        # set the head to the current previous_node which would be the last node in the initial list
        self.head = previous_node
