class Solution:
    def minSwaps(self, s: str) -> int:
        current_Balance = 0  # Variable to keep track of the balance of brackets
        negative_Balance_Count = 0  # Count of how many times the balance goes negative

        # Iterate through each character in the string
        for character in s:
            if character == '[': 
                current_Balance += 1  # Increment balance for opening bracket
            else: 
                current_Balance -= 1  # Decrement balance for closing bracket

            # Check if the current balance is negative
            if current_Balance < 0: 
                negative_Balance_Count += 1  # Increment the negative balance count
                current_Balance = 0  # Reset balance to 0 since we've accounted for the imbalance

        # Calculate minimum swaps needed to balance the string
        # Each two negative balances can be fixed by one swap
        return (negative_Balance_Count + 1) // 2

# Time Complexity: O(n), where n is the length of the string `s`.
# We make a single pass through the string, performing constant-time operations.

# Space Complexity: O(1), since we are using a fixed amount of extra space (only a few variables).