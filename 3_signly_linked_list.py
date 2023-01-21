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
        print('self.head : if list is not empty', self.head)
        new_node.next_node = self.head;
        self.head = new_node;


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


