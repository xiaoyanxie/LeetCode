from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for str in strs:
            # count = [0] * 26
            # for c in str:
            #     count[ord(c) - ord('a')] += 1
            # mp[tuple(count)].append(str)
            mp[''.join(sorted(str))].append(str)

        return [mp[key] for key in mp]
