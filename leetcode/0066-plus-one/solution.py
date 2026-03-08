class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] < 10:
            return digits
        
        """
        [1,5,0,0,0], carry = 0
      i
        
        """
        digits[-1] -= 10
        carry = 1
        for i in reversed(range(0, len(digits) - 1)):
            digits[i] += carry
            if digits[i] >= 10:
                digits[i] -= 10
            else:
                carry = 0
            # print(f'digits[{i}] = {digits[i]}, carry={carry}')

        if carry == 0:
            return digits
        
        return [1] + digits
