class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            anagram = ''.join(sorted(i))
            if anagram in anagrams:
                anagrams[anagram] = anagrams[anagram] + [i]
                pass
            else:
                anagrams[anagram] = [i]
        
        return list(anagrams.values())