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


"Call Node class with instance N1 "
""" Nodes are building blocks of list(python) """
N1 = Node(10);
print("Value of N1 is : ")
print(N1)

"Call 2nd node N2"
N2 = Node(20);

"Set next node of N1 which is N2"
N1.next_node=N2;

print(N1.next_node)


