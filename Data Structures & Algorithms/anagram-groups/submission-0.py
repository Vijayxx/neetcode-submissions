class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for i in range(len(strs)):
            count = [0]*26
            for j in strs[i]:
                count[ord(j) - ord('a')] += 1
            
            key = tuple(count)

            if key not in h:
                h[key] = []
            
            h[key].append(strs[i])
        
        return list(h.values())

        