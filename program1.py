

from typing import List

def smallest_missing_positive_integer(nums: List[int]) -> int:
    """
    Finds the smallest missing positive integer in the given list.

    Parameters:
        nums (List[int]): A list of integers.

    Returns:
        int: The smallest missing positive integer.
    """
    if not nums:
        return 1
    
    # Separate positive integers
    positive_integers = [x for x in nums if x > 0]
    
    # If there are no positive integers, 1 is the smallest missing positive integer
    if not positive_integers:
        return 1
    
    # Use a set to efficiently check for presence of integers
    integer_set = set(positive_integers)
    
    # Start from 1 and check for the smallest missing positive integer
    i = 1
    while True:
        if i not in integer_set:
            return i
        i += 1

# Example usage:
nums = [3, 4, -1, 1]
print(smallest_missing_positive_integer(nums))  # Output: 2






    



  

