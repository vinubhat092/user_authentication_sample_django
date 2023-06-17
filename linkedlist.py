class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def print(self):
        current = self.head
        llstr = ''
        while current:
            llstr += str(current.data) + ' ---> '
            current = current.next
        print(llstr)


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.head = Node(0)
    linked_list.head.next = Node(1)
    linked_list.head.next.next = Node(1)
    linked_list.head.next.next.next = Node(3)
    linked_list.reverse()
    linked_list.print()