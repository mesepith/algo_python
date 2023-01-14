""" Binary search has complexity of O(log n), since it has to go through half of the elements in the array to find the target element. """

"Binary search is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the array. Binary search runs in logarithmic time in the worst case, making O(log n) comparisons, where n is the number of elements in the array, and therefore is very efficient for large arrays. "

"Binary search array must be sorted. If the array is not sorted, the result will be undefined. Binary search is faster than linear search, except for small arrays. Binary search is also known as half-interval search, logarithmic search, or binary chop. "

"O(log n) is the complexity of binary search. O(log n) means that the number of operations is proportional to the logarithm of the input size. The logarithm of a number roughly measures the number of times you can divide that number by 2 before you get a value that's less than or equal to 1. "


def binary_search(arr, target):

    print('target : ', target)

    first = 0
    last = len(arr)-1


    while(first<=last):

        mid = (first+last)//2

        if(arr[mid]==target):
            return mid
        elif(arr[mid] <target):
            first = mid+1
        else:
            last = mid-1
    
    return None

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def verify(index):

    print("List is: ", numbers)

    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

    print("")


result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)

result = binary_search(numbers, 8)
verify(result)

result = binary_search(numbers, 2)
verify(result)