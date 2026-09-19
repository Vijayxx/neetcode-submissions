class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s += f"{len(i)}á{i}"
        return s

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != "á":
                j += 1

            length = int(s[i:j])

            l.append(s[j+1:j+1+length])

            i = j + 1 + length
        return l

