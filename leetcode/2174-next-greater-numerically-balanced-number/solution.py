class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        if n == 0:
            return 1

        def numDigits():
            digits = 0
            m = n
            while m > 0:
                digits += 1
                m //= 10
            return digits

        def generate(digits):
            if digits == 0:
                return []
            num = str(digits) * digits
            numbers = [num]
            for k in range(digits // 2 + 1):
                left = str(digits - k) * (digits - k)
                for right in generate(k):
                    if left == right:
                        continue
                    numbers.append(left + right)
            return numbers
        
        groups = { i: generate(i) for i in range(1, 8) }

        digits = numDigits()
        if n >= int(str(digits) * digits):
            digits += 1
        
        possibleNumbers = set()
        for nums in groups[digits]:
            for candidate in itertools.permutations(nums):
                possibleNumbers.add(int(''.join(candidate)))

        numbers = sorted(list(possibleNumbers))
        i = bisect.bisect_right(numbers, n)
        return numbers[i]
