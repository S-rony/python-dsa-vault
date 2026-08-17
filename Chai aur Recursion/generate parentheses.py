from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtracking(current: str,open_left: int, close_left: int):
            # base case
            if open_left == 0 and close_left == 0:
                result.append(current)
                return

            if open_left > 0:
                backtracking(current + "(", open_left - 1, close_left)

            if close_left > open_left:
                backtracking(current +")", open_left, close_left - 1)

        backtracking("",n,n)
        return result

