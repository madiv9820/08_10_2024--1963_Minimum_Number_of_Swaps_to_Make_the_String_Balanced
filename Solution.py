class Solution:
    def minSwaps(self, s: str) -> int:
        character_Stack = []  # Stack to keep track of unmatched opening brackets

        # Iterate through each character in the string
        for character in s:
            if character == '[':
                character_Stack.append(character)  # Push opening brackets onto the stack
            elif len(character_Stack) > 0:
                character_Stack.pop()  # Pop matching opening bracket for each closing bracket

        # The number of unmatched opening brackets left in the stack determines the swaps needed
        # Each two unmatched brackets can be fixed by one swap
        return (len(character_Stack) + 1) // 2

# Time Complexity: O(n), where n is the length of the string `s`.
# We make a single pass through the string, performing constant-time operations.

# Space Complexity: O(n) in the worst case, where all characters are '[' and none are ']'.
# The stack can grow to hold all opening brackets if the string is heavily unbalanced.