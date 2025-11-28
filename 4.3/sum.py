# Exercise 2: Sum of Integers
# Write a function named sum_list_recursive(numbers, index) that
# takes a list of integers and an index and returns their sum.
# Remember that the sum of a list is the first item plus the sum of the rest of the list.

def sum_list_recursive_helper(numbers, index):
    
    return 0

def sum_list(numbers):
    if len(numbers) > 0:
        return sum_list_recursive_helper(numbers, 0)
    return 0

# Test cases
print(sum_list([1, 2, 3, 4]))   # Expected output: 10
print(sum_list([-1, 1, 2]))     # Expected output: 2
print(sum_list([5, 10, 15]))    # Expected output: 30