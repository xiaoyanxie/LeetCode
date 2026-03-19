class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        find one anagram->iterate
        eat
        ^
        a1
        e1
        t1

        tea
        """

        table = collections.defaultdict(list)
        for str in strs:
            # newStr = "".join(sorted(str))
            # table[newStr].append(str)
            count = [0] *26
            for c in str:
                count[ord(c) - ord("a")] += 1
            table[tuple(count)].append(str)

        # res = []
        # for key in table.keys():
        #     ana = list(table[key])
        #     res.append(ana)
        return list(table.values())
            

