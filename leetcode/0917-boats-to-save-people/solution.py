class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        boat: 3
        1,2,2,3, limit=3
          i
          j
        """

        people.sort()
        boats = 0
        i, j = 0, len(people) - 1
        while i < j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            
            boats += 1
        
        if i == j:
            boats += 1

        return boats
            
