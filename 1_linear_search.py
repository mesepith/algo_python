def linear_search(arr, target):
    """Return the index position of the target if found, else return None"""
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return None   # not found


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
""" concat in python """
print("numbers: " + str(numbers));

print("11 is found in : ")
print(linear_search(numbers, 11))  # None

print("5 is found in : ")
print(linear_search(numbers, 5))  # 4


   


