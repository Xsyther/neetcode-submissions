class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        j = 0 
        
        for i in range(1,len(nums)): 
            start = nums[j]
            if start == nums[i] :
                return True
            else :
                j = j+1
                start = nums[j]


        return False