class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = dict()
        for i in strs:
            t = ''.join(sorted(i))
            if t not in r:
                r[t] = []

            r[t].append(i)

        return list(r.values())

            