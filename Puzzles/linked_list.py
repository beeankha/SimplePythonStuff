# https://realpython.com/linked-lists-python/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        # The only information you need to store for a linked list is
        # where the list starts (the head of the list)
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

list1 = LinkedList()
print(list1)  # output should be "None" ✅

first_node = Node("a")
list1.head = first_node
print(list1)  # output should be "a - > None" ✅

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(list1)  # output should be "a -> b -> c -> None" ✅

list1 = LinkedList(["a", "b", "c", "d", "e"])
print(list1)  # output should be "a -> b -> c -> d -> e -> None" ✅

for node in list1:
    print(node)  # ✅

# Stopped at: "How to Insert a New Node"
# https://realpython.com/linked-lists-python/#how-to-insert-a-new-node
