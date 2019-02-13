# Given an array of integers values of 0, 1, and 2, sort them in linear time. 
# 
# Input: Array of Integers where elements values belong to the set S : { 0, 1, 2 }
# Output: Sorted Array
# 
# Linear time O(n)
# 

# if list is empty > return []
# list will only have numbers in the range of 0-2  
# 

# Since there are only three numbers, take 1 as placeholder

# Input: [2, 0, 1, 2, 1, 0] => [0, 0, 1, 1, 2, 2]


# [2, 0, 1, 2, 1, 0]

# If the number is a 2, pop and append
# if the number is a 0, insert at beginning


def sort_zeros_twos(list_nums):

    for i in range(0, len(list_nums)):
        if list_nums[i] == 0: 
            list_nums.insert(0, list_nums.pop(i))
        elif list_nums[i] == 2:
            list_nums.append(list_nums.pop(i))

    return list_nums


print(sort_zeros_twos([2, 0, 1, 2, 1, 0]))