class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
            stack.append(i)

        return res
