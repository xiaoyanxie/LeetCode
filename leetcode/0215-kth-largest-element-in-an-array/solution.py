class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        
        left, mid, right = [], [], []
        for n in nums:
            if n < pivot:
                left.append(n)
            elif n > pivot:
                right.append(n)
            else:
                mid.append(n)
        
        """
          L         M      R
        | 1,2,3 | 4,4,4 | 5,6,7 |
           k: self.findKthLargest(left, k - len(mid) - len(right))
                   k: return pivot
                           k: self.findKthLargest(right, k)
        """
        if len(right) < k <= len(mid) + len(right):
            return pivot
        elif k <= len(right):
            return self.findKthLargest(right, k)
        else:
            return self.findKthLargest(left, k - len(mid) - len(right))
