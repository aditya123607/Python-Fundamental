class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

node1 = Node(59)
node2 = Node(65)
node3 = Node(70)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

new_node = Node(25)
new_node.next = node2.next
new_node.prev = node2
node2.next.prev = new_node
node2.next = new_node
current = node1

while current is not None:
    print(current.data,end = " -> ")
    current = current.next
print("none")