class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        countNums = {}

        for i in range(len(nums)):
            countNums[nums[i]] = 1 + countNums.get(nums[i], 0)

            if countNums[nums[i]] > 1:
                return True

        return False
        