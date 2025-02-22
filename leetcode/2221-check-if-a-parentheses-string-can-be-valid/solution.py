class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        #check the number of parenthesis is even
        if len(s) % 2 != 0:
            return False
        #check if the parenthesis meet the rquirement before changing using stack

# First pass: check if the right ) can be paired up with enough ( or flipable ones
        counter = 0
        for i in range(len(s)):
            if s[i] == "(" or locked[i] == '0':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
# Second pass: check if the left ( can be paired up with enough ) or fipable ones            
        counter2 = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ")" or locked[i] == '0':
                counter2 += 1
            else:
                counter2 -= 1

            if counter2 < 0:
                return False

        return True


        #change
