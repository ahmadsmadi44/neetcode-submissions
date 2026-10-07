class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # 26 spaces , [0] * 26
        res = defaultdict(list)
        for s in strs: # loop thru every word
            count = [0] * 26

            for c in s: #loop thru ever char in every word
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())

