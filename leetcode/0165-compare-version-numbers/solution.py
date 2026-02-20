class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.') # 1.0
        v2 = version2.split('.') # 1.0.0.0
        len1 = len(v1)
        len2 = len(v2)
        i = 0
        while i < min(len1, len2):
            a, b = int(v1[i]), int(v2[i])
            i += 1
            if a > b:
                return 1
            elif a < b:
                return -1
        
        if len1 == len2:
            return 0

        while i < len1:
            if int(v1[i]) > 0:
                return 1
            i += 1
        
        while i < len2:
            if int(v2[i]) > 0:
                return -1
            i += 1

        return 0
