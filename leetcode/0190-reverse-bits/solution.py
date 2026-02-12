class Solution:
    def reverseBits(self, n: int) -> int:
        # print(0b101)
        # print(0b101 | 0b010)
        # print(0b10100101000001111010011100 & 0b100000)
        # print(bin(0b001 << 2))
        # print(bin(~(1 << 4)))
        # print(bin(abs(~0b0011)))
        # a = 0b1001
        # mask = (1 << 32) - 1
        # print(bin(mask))
        # print(bin(n))
        # print(bin(n ^ mask))
        # """
        # 0b10100101000001111010011100
        # 0b01011010111110000101100011
        # """
        
        # mask = (1 << 32) - 1
        # return n ^ mask
        # print(bin(mask))
        # print(bin(n))
        # for i in range(32):
        #     if n & mask == 0: # if bit is 1
        #         n = n & ~(1 << i)# make it 0
        #     else: # if bit is 0
        #         n = n | mask # make it 1
        #     mask = mask << 1 # move mask left to test the next bit
        # print(bin(n))
        
        # print(bin(0b00000000000000000000000000000001 << 31))
        # """
        # 00000000000000000000000000000001
        # 00000010100101000001111010011100
        # ^                              ^
        
        # """
        leftMask = 1 << 31
        rightMask = 1
        for i in range(16):
            if (leftMask & n > 0 and rightMask & n == 0) or (leftMask & n == 0 and rightMask & n > 0):
                # left is 1, right is 0
                # left is 0, right is 1
                n ^= leftMask
                n ^= rightMask
            leftMask = leftMask >> 1
            rightMask = rightMask << 1
        return n


        # res = 0
        # for _ in range(32):
        #     res = (res << 1) | (n & 1)
        #     n = n >> 1
        # return res

        # return int(bin(n)[2:].zfill(32)[::-1], 2)
                
                

