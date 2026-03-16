from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        ["eat","tea","tan","ate","nat","bat"]

        {
            'aet': ['eat','tea', 'ate']
            'ant': ['tan', 'nat']
            'abt': ['bat']
        }
        """
        groups = defaultdict(list)

        for s in strs:
            groups[''.join(sorted(s))].append(s)
        
        return [ groups[key] for key in groups ]
