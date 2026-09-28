class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) - 1 <= k:
            return len(nums) != len(set(nums))

        dictionary = {}

        for index, num in enumerate(nums):
            if num in dictionary:
                if index - dictionary[num] <= k:
                    return True

            dictionary[num] = index

        return False