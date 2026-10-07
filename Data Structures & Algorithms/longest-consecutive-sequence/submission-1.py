class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # make a set
        # initialize longest to 0
        # for loop, check if -1 is there if not then longest = 1
        # if it is then do while num + length are in the set keep adding 1

        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length +=1
                longest = max(length, longest)
        return longest