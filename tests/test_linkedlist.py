from datastrucures.linkedlist import LinkedList, Node
import unittest

class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
        self.node1 = Node("3")
        self.node2 = Node("2")
        self.node3 = Node("4")
        self.ll.append(self.node1)
        self.ll.append(self.node2)
        self.ll.append(self.node3)
        

    def test_append(self):
        self.assertEqual("324", self.ll.printlinkedlist())

    def test_insert(self):
        self.ll.insert(self.node1, Node("5"))
        self.assertEqual("3524", self.ll.printlinkedlist())

    def test_push(self):
        self.ll.push(Node("10"))
        self.assertEqual("10324", self.ll.printlinkedlist())

if __name__ == "__main__":
    unittest.main()
    
