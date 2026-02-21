class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        """
        10,11,12,13,14,15,16,17,......20,21,22

        1 digit : 1
        2 digits: 22
        3 digits: 122, 221, 333
        4 digits: 1333, 3331, 4444
        5 digits: 14444, 22333, 33322, 44441, 55555



        123: 123 - 1230
        """

        combinations = [
            [1],
            [2,2],
            [1,2,2],[3,3,3],
            [1,3,3,3],[4,4,4,4],
            [1,4,4,4,4],[2,2,3,3,3],[5,5,5,5,5],
            [1,2,2,3,3,3],[4,4,4,4,2,2],[5,5,5,5,5,1],[6,6,6,6,6,6],
            [1,2,2,4,4,4,4]
        ]

        nums = []
        for combo in combinations:
            for p in set(itertools.permutations(combo)):
                num = int(''.join(map(str, p)))
                nums.append(num)

        nums.sort()

        for num in nums:
            if num > n:
                return num

        # def isBalanced(x):
        #     xs = str(x)
        #     cnt = Counter(xs)
        #     for d in cnt:
        #        if cnt[d] != int(d):
        #          return False
        #     return True

        # def search(l, r):
        #     if l < r:
        #         return None
        #     mid = l + (r - l) // 2
        #     if isBalanced(mid):
        #         return mid
        #     left = search(l, mid - 1)
        #     if left:
        #         return left
        #     return search(mid + 1, r)
        
        # return search()
        # def maxAt(x):
        #     s = str(x)
        #     return int(str(len(s)) * len(s))

        # def nextN(x):
        #     s = str(x)
        #     return 10**(len(s))

        # n += 1
        # maxN = n * 100
        # while n < maxN:
        #     if isBalanced(n):
        #         return n
        #     if n > maxAt(n):
        #         n = nextN(n)
        #     else:
        #         n += 1
