Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


1. Initialize an empty list `ans_list` to store intermediate combinations during backtracking.

2. Define a nested function `backtracking(p, n, r)` that handles the backtracking process.

   - `p` represents the count of remaining open parentheses.
   - `n` represents the count of remaining close parentheses.
   - `r` is a list that accumulates the current combination being constructed.

3. Inside the `backtracking` function:
   - If `p` and `n` are both zero, the accumulated combination `r` is added to the `ans_list` as it represents a valid combination of parentheses.
   - If the last element of `r` is negative, this means there are more close parentheses than open parentheses, so the function iterates through the range from 1 to `p + 1` to explore possibilities of adding open parentheses.
   - If the last element of `r` is non-negative, the function iterates through the range from 1 to the sum of all elements in `r` + 1 to explore possibilities of adding close parentheses.

4. In the outer loop that iterates through the range from 1 to `n + 1`, the `backtracking` function is called with appropriate initial values to start constructing combinations.

5. After backtracking is complete, the code constructs the final result list `res`. It iterates through each combination in `ans_list` and converts it to a string format with open and close parentheses, and then appends it to `res`.

6. The final `res` list is reversed to ensure that the combinations are returned in the correct order.

7. The function returns the `res` list containing all possible combinations of well-formed parentheses.
