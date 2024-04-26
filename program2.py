
def longest_substring(s: str) -> int:
    # Initialize variables
    max_length = 0
    left = 0
    char_index_map = {}
    
    # Iterate through the string
    for right, char in enumerate(s):
        # If the character is already in the map and its index is after the left boundary,
        # update the left boundary to the index after the last occurrence of the character
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1
        
        # Update the index of the current character in the map
        char_index_map[char] = right
        
        # Update the maximum length of the substring
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example usage:
input_string = "abcabcbb"
print(longest_substring(input_string))  # Output: 3







