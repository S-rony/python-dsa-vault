from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtracking(start: int, current: List[int], total: int):
            if total == target:
                result.append(list(current))
            if total > target:
                return
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtracking(i, current, total + candidates[i])
                current.pop()

        backtracking(0,[], 0)
        return result