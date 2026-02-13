class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        mx = max(nums)
        freq = [0] * (mx + 1)

        for num in nums:
            freq[num] += 1

        index = 0
        for value in range(mx + 1):
            while freq[value] > 0:
                nums[index] = value
                index += 1
                freq[value] -= 1



        