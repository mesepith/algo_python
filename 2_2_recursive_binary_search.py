def recursive_binary_search(list, target):

    print(' ')
    print('list ', list)
    print('Length of list : ' , len(list))

    if(len(list)==0):
        return False;
    else:
        mid = ((len(list))//2);

        if(list[mid]==target):
            return True;

        elif(list[mid]<target):
            print('mid value is smaller than target, mid value is', list[mid])
            return recursive_binary_search(list[mid+1:], target)
        
        elif(list[mid]>target):
            print('mid value is greater than target mid value is', list[mid])
            return recursive_binary_search(list[:mid], target)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('numbers are ', numbers)
print('')

def verify(result):
    print('Result is : ', result)
    print(' ')
    print(' ')

looking_for = 12
print('############### Looking for : ', looking_for)
result = recursive_binary_search(numbers, looking_for)
verify(result)

looking_for = 6
print('############### Looking for : ', looking_for)
result = recursive_binary_search(numbers, looking_for)
verify(result)

looking_for = 8
print('############### Looking for : ', looking_for)
result = recursive_binary_search(numbers, looking_for)
verify(result)

looking_for = 2
print('############### Looking for : ', looking_for)
result = recursive_binary_search(numbers, looking_for)
verify(result)
