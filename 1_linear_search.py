""" Linear Search Algorithm has complexity of O(n), since it has to go through all the elements in the array to find the target element. """
def linear_search(arr, target):
    """Return the index position of the target if found, else return None"""
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return None   # not found

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def verify(index):

    print("")

    print("List is: ", numbers)

    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)
   


