class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 # intialize max area
        stack = [] # index : height

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # loop while stack is not empty and top of stack > current h
                index, height = stack.pop() # remove top pair
                maxArea = max(maxArea, height * (i - index)) # calc rect area for that height
                start = index # move start further left
            stack.append((start, h)) # add current height to the stack

        for i, h in stack: # after going thru all the heights, loop anything left in the stack
            maxArea = max(maxArea, h * (len(heights) - i)) # calc remaining area
        return maxArea


