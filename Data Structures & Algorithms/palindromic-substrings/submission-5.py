class Solution:
    def countSubstrings(self, s: str) -> int:
        n= len(s)
        count = 0

        for i in range(n):
            for j in range(i,n):
                if s[i:j] == s[j:i:-1]:
                    count += 1

        return count
                