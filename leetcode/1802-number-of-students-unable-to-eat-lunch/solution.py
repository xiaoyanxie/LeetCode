class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        size = len(students)
        cnt0 = 0
        cnt1 = 0
        
        for s in students:
            if s == 0:
                cnt0 += 1 
            else:
                cnt1 += 1

        for i, san in enumerate(sandwiches): 
            if san == 0 and cnt0 == 0:
                return size - i
            if san == 1 and cnt1 == 0:
                return size - i
            
            if san == 0:
                cnt0 -=1
            else:
                cnt1 -=1
        
        return 0

