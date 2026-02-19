class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # queue
        #0, 1, .... n-1
        #person : i , #tickets : tickets[i] 
        #[0,1,0] time: 6 i 6%3 = 0
        #     ^
        # time = 0
        # i = 0
        # while tickets[k] != 0:
        #     if tickets[i] == 0:
        #         i = (i + 1) % len(tickets)
        #         continue
        #     if tickets[i] != 0:
        #         tickets[i] -= 1
        #         time += 1
            
        #     i = (i + 1) % len(tickets)
        # return time
        time = 0
        for i in range(len(tickets)):
            if i <= k :
                time += min(tickets[i], tickets[k])

            else:
                time += min(tickets[i], tickets[k] - 1)
        return time
