class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def delete(self):
        if self.head is None:
            return print("This list is empty")

        if self.head.next is None:
            self.head = None
        else:
            current_node = self.head
            while current_node.next is not None:
                self.tail = current_node
                current_node = current_node.next
            self.tail.next = None

    def rollout(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.prepend(0)
    linked_list.rollout()