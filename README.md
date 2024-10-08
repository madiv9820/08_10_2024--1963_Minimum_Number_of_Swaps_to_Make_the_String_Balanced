# 1963. Minimum Number of Swaps to Make the String Balanced

__Type:__ Medium <br>
__Topics:__ Two Pointers, String, Stack, Greedy <br>
__Companies:__ Meta, Amazon, Expedia, Apple, Visa, Twilio <br>
__Leetcode Link:__ [Minimum Number of Swaps to Make the String Balanced](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/)
<hr>

You are given a __0-indexed__ string `s` of __even__ length `n`. The string consists of __exactly__ `n / 2` opening brackets `'['` and `n / 2` closing brackets `']'`.<br><br>
A string is called __balanced__ if and only if:
- It is the empty string, or
- It can be written as `AB`, where both `A` and `B` are __balanced__ strings, or
- It can be written as `[C]`, where `C` is a __balanced__ string.

You may swap the brackets at __any__ two indices __any__ number of times. <br><br>
Return _the __minimum__ number of swaps to make_ s ___balanced___.
<hr>

### Examples

__Example 1:__ <br>
__Input:__ s = "][][" <br>
__Output:__ 1 <br>
__Explanation:__ You can make the string balanced by swapping index 0 with index 3. <br>
The resulting string is "[[]]".

__Example 2:__ <br>
__Input:__ s = "]]][[[" <br>
__Output:__ 2 <br>
__Explanation:__ You can do the following to make the string balanced: 
- Swap index 0 with index 4. s = "[]][][".
- Swap index 1 with index 5. s = "[[][]]".

The resulting string is "[[][]]".

__Example 3:__ <br>
__Input:__ s = "[]" <br>
__Output:__ 0 <br>
__Explanation:__ The string is already balanced.
<hr>

### Constraints:

- `n == s.length`
- <code>2 <= n <= 10<sup>6</sup></code>
- `n` is even.
- `s[i]` is either `'['` or `']'`.
- The number of opening brackets `'['` equals `n / 2`, and the number of closing brackets `']'` equals `n / 2`.
<hr>

### Hints:
- Iterate over the string and keep track of the number of opening and closing brackets on each step.
- If the number of closing brackets is ever larger, you need to make a swap.
- Swap it with the opening bracket closest to the end of s.