#TC: O(n)
#SC: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        if len(nums) == 1 or len(nums) ==2:
            return max(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        
        return dp[-1]