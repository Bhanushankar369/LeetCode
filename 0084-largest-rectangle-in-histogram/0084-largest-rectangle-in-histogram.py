class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        startInd = [-1]*len(heights)
        endInd = [-1]*len(heights)

        # endind of the particular point
        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                endInd[j] = i-1

            stack.append(i)

        for i in range(len(endInd)):
            if endInd[i] == -1:
                endInd[i] = len(heights)-1


        # startind of a particular point
        stack = []

        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                startInd[j] = i+1

            stack.append(i)

        for i in range(len(startInd)):
            if startInd[i] == -1:
                startInd[i] = 0
        
        # max from both sides
        maxi = 0
        for i in range(len(heights)):
            maxi = max(maxi, (endInd[i]-startInd[i]+1)*heights[i])
        
        return maxi