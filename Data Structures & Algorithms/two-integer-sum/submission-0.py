class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:      
        hashmap = {}

        for index, element in enumerate(nums):
            difference = target - element
            if difference in hashmap:
                return [hashmap[difference], index]
            else:
                hashmap[element] = index