class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        sorted_freq = sorted(frequency.items(), key=lambda pair: pair[1], reverse = True)
        return [item[0] for item in sorted_freq[:k]]