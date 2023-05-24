"""
File to practice with Linked list
"""

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, node: Node):
        """
        Push to begin
        """
        if self.head is None:
            self.head = node
            return
        
        node.next = self.head
        self.head = node


    def append(self, node: Node):
        """
        Append to the end
        """

        if self.head is None:
            self.head = node
            return

        dummy = self.head
        while dummy.next:
            dummy = dummy.next

        dummy.next = node


    def insert(self, prev_node: Node, node: Node):
        """
        Insert after prev_node
        """
        node.next = prev_node.next
        prev_node.next = node


    def printlinkedlist(self):
        """
        Traversal linkedList
        """
        dummy = self.head
        res = []

        while dummy:
            res.append(dummy.data)
            dummy = dummy.next

        return "".join(res)

if __name__ == "__main__":
    pass