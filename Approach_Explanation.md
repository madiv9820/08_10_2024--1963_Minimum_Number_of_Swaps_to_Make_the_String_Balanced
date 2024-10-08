# Minimum Swaps to Balance Brackets: Two Approaches

- ## Approach 1: Stack Method

    - ### Intuition
        - Use a stack to track unmatched opening brackets. Each unmatched closing bracket reduces the count of unmatched opening brackets. This allows us to count the necessary swaps to balance the string.

    - ### Approach
        1. Initialize an empty stack.
        2. Iterate through the string:
            - Push `[` onto the stack for each opening bracket.
            - For each closing bracket `]`, pop the stack if it’s not empty (matching it with an opening bracket).
        3. The number of unmatched opening brackets left in the stack indicates how many swaps are needed:
        
        Return `(len(character_Stack) + 1) // 2` for the minimum swaps.

    - ### Time Complexity
        - **O(n)**: Single pass through the string.

    - ### Space Complexity
        - **O(n)**: In the worst case, the stack can hold all opening brackets.

    - ### Code
        ```python
        class Solution:
            def minSwaps(self, s: str) -> int:
                character_Stack = []  # Stack to keep track of unmatched opening brackets

                # Iterate through each character in the string
                for character in s:
                    if character == '[':
                        character_Stack.append(character)  # Push opening brackets onto the stack
                    elif len(character_Stack) > 0:
                        character_Stack.pop()  # Pop matching opening bracket for each closing bracket

                # Calculate the minimum swaps needed based on unmatched opening brackets
                return (len(character_Stack) + 1) // 2
        ```

- ## Approach 2: Balance Count Method

    - ### Intuition
        - Track the balance of brackets as you iterate through the string. Count how many times the balance goes negative to determine the number of swaps needed to balance the string.

    - ### Approach
        1. Initialize `current_Balance` and `negative_Balance_Count`.
        2. Iterate through the string:
            - Increment for `[` and decrement for `]`.
            - If balance is negative, increment the negative count and reset balance.
        3. Return `(negative_Balance_Count + 1) // 2` for the minimum swaps.

    - ### Time Complexity
        - **O(n)**: Single pass through the string.

    - ### Space Complexity
        - **O(1)**: Only a few variables used for counting.

    - ### Code
        ```python
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
                return (negative_Balance_Count + 1) // 2
        ```