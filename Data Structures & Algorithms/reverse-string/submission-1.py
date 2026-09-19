class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        index = 0
        while index+1 <= len(s)/2:
            tmp = s[index]
            s[index] = s[len(s)-1-index]
            s[len(s)-1-index] = tmp
            index+=1

        return s
        