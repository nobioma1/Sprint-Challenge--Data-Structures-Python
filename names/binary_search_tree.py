class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current_node = self.value
        # LEFT CASE
        # check if the new nodes value is less than our current ones value
        if value < current_node:
            # if the is no left child
            if self.left is None:
                # place a new node here
                self.left = BinarySearchTree(value)
                return
            # otherwise
            else:
                # repeat process for left
                left_node = self.left
                left_node.insert(value)

        # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current parent value
        if value >= current_node:
            # if there is no right child here
            if self.right is None:
                # place a new one
                self.right = BinarySearchTree(value)
                return
            # otherwise
            else:
                # repeat process right
                right_node = self.right
                right_node.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        current_node = self.value

        # Check if target is equal to root node
        if current_node == target:
            return True

        # Check if target is less than target
        if target < current_node:
            # return false if there's no other child node to the left
            if self.left is None:
                return False
            # otherwise
            else:
                left_node = self.left
                # check if the left node contains the target
                return left_node.contains(target)

        # Check if target is greater than target
        if target >= current_node:
            # return false if there's no other node to the right
            if self.right is None:
                return False
            # otherwise
            else:
                right_node = self.right
                # check if the right node contains target
                return right_node.contains(target)

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # check if the value is not none
        if self.value != None:
            # Call cb and pass the current value
            cb(self.value)
            # if the left of the current node is not None
            if self.left != None:
                # Call the for_each method on the left node passing the cb
                self.left.for_each(cb)
            # if the right of the current node is not None
            if self.right != None:
                # Call the for_each method on the right node passing the cb
                self.right.for_each(cb)
