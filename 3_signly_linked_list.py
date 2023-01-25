""" Singly linked list implementation in Python """

""" first we create a class to represent node """
class Node:

    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """

    "create two instance variable one is data to store data and 2nd one is  next_node to point to the next node in the list"
    dataz1= None;
    next_node= None;

    "add constructor this class easy to create"
    def __init__(self,dataz2):
        "assign data to instance variable data "

        self.dataz1=dataz2;

    "create wrapper function to get readable data"
    def __repr__(self):
        return "<Node data: %s>" %self.dataz1;

class LinkedList:

    """
    Singly linked list
    """

    "create instance variable to store head node of the list"
    head = None;

    "create constructor to create list"
    def __init__(self):
        self.head = None;

    "create wrapper function to get readable data"
    def __repr__(self):
        nodes = [];
        current_node = self.head;
        while current_node:
            if current_node is self.head:
                nodes.append("[Head: %s]" %current_node.dataz1);
            elif current_node.next_node is None:
                nodes.append("[Tail: %s]" %current_node.dataz1);
            else:
                nodes.append("[%s]" %current_node.dataz1);
            current_node = current_node.next_node;
        return '-> '.join(nodes);

    "create function to add node at the beginning of the list"
    def add_node_at_beginning(self,dataz4):
        print()
        "create new"
        new_node = Node(dataz4);
        "check if list is empty"
        print('new_node ', new_node)
        print('self.head ', self.head)
        if self.head is None:
            self.head = new_node;
            print(' self.head or new_node ', new_node)
            return;
        "if list is not empty"
        new_node.next_node = self.head;
        print('new_node.next_node at end:  ', new_node.next_node)
        print('new_node.next_node.next_node at end:  ', new_node.next_node.next_node)
        self.head = new_node;

        print('self.head at end:  ', self.head);
        print('self.head.next_node: ', self.head.next_node)
        print('self.head.next_node.next_node: ', self.head.next_node.next_node)

        print('##### self start #######')
        print(self)
        print('##### self end #######')

    "create function to add node at the end of the list"
    def add_node_at_end(self,dataz5):
        "create new"
        new_node = Node(dataz5);
        "check if list is empty"
        if self.head is None:
            self.head = new_node;
            return;
        "if list is not empty"
        current_node = self.head;
        while current_node.next_node:
            current_node = current_node.next_node;
        current_node.next_node = new_node;


    """ search for a node with data and return the node if found """
    def search(self, key):
        current_node = self.head;
        while current_node:
            if current_node.dataz1 == key:
                return current_node;
            else:
                current_node = current_node.next_node;
        return None;
        

print();

 #call add_node_at_beginning function
L1 = LinkedList();
L1.add_node_at_beginning(10);
L1.add_node_at_beginning(20);
L1.add_node_at_beginning(30);
L1.add_node_at_beginning(40);
L1.add_node_at_beginning(50);
print()
print("Value of L1 which is calling add_node_at_beginning fun is : ")
print(L1)

print();

#call add_node_at_end function
L2 = LinkedList();
L2.add_node_at_end(10);
L2.add_node_at_end(20);
L2.add_node_at_end(30);
L2.add_node_at_end(40);
L2.add_node_at_end(50);
print("Value of L2 which is calling add_node_at_end fun is : ")
print(L2)

