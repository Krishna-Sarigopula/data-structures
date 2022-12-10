class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.node = None
        self.tail = None

    def traverseList(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def insertNode(self, value, index):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if index == 0:
                newNode.next = self.head
                self.head = newNode
            elif index == -1:
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                count = 0
                while count < index - 1:
                    tempNode = tempNode.next
                    count += 1
                nextnode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextnode


singleLinkedList = SingleLinkedList()
singleLinkedList.insertNode(10, 1)
singleLinkedList.insertNode(30, 1)
singleLinkedList.insertNode(40, 1)
singleLinkedList.insertNode(20, 1)


singleLinkedList.traverseList()
