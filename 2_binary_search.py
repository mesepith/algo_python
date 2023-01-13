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