class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # nums = [ i for i in range(1, n + 1)]
        res = []
        def backtracking(path, idx):
            if len(path) == k:
                res.append(list(path))
                return
            
            for i in range(idx, n - (k - len(path)) + 2):
                path.append(i)
            
                backtracking(path, i+1)
                path.pop()
        
        backtracking([], 1)
        return res


