class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        # make a hash map for letter and frequency
        if len(s) <= 1:
            return [s]

        from collections import Counter
        hmap = Counter(s)
        odd = []
        
        for key in hmap.keys(): 
            if hmap[key] % 2 != 0:
                odd.append(key)
                if len(odd) > 1:
                    return []

        for key in hmap.keys():
            hmap[key] //= 2
        midChar = odd[0] if odd else ""
        # select diff letters for the ith slot for the palindrome
        res = []
        def backtrack(path, hmap):
            if len(path) == len(s)//2:
                path = "".join(path)
                res.append(path + midChar + path[::-1])
                return
                
            for key in hmap.keys():
                if hmap[key] > 0:
                    path.append(key)
                    hmap[key] -= 1
                    backtrack(path, hmap)
                    path.pop()
                    hmap[key] += 1
            return res
                
        return backtrack([],hmap)


