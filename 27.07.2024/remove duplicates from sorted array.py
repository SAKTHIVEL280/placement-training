class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i ,j = 0,1
        l = len(nums)
        while j<l:
            if nums[j] == nums[i]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1
                j += 1   
        return i+1  
