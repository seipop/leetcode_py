class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tnums = {nums[0]: 0}
        for i in range(1, len(nums)):
            t = target - nums[i]
            if t in tnums:
                return [tnums[t], i]
            else:
                tnums.update({nums[i]: i})

if __name__ == '__main__':
    solution = Solution()
    r = solution.twoSum([1, 2, 3], 3)
    print r
