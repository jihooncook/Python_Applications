def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

#Testing the code
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3)) # Should print 1 because it is located in the index 1 of my_list
print(binary_search(my_list, -1)) # Should print None because -1 does not exist in my_list