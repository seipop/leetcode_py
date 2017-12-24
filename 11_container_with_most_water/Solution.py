class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        low = 0
        high = len(height) - 1

        while low < high:
            maxArea = max(maxArea, (high - low) * min(height[low], height[high]))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return maxArea
