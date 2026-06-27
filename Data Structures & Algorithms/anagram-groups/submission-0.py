class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l= defaultdict(list)

        for i in strs:
            sorteds= ''.join(sorted(i))
            l[sorteds].append(i)
        return list(l.values())