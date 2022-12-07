class Node:
    def __init__(self, value=None) -> None:
        self.next = None
        self.value = value


class singleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.node = None
        self.tail = None


sList = singleLinkedList()
node = Node(1)
node1 = Node(2)
node2 = Node(3)

sList.head = node
sList.head.next = node1
sList.node = node1
sList.node.next = node2
