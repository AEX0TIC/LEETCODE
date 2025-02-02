class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # Dictionary to store number and its index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_map:
                return [num_map[complement], i]  # Return indices if complement is found
            
            num_map[num] = i  # Store index of the current number
        
        return []  # Should never reach here as per the problem constraints

# Example usage:
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))  # Output: [0,1]
print(solution.twoSum([3,2,4], 6))      # Output: [1,2]
print(solution.twoSum([3,3], 6))        # Output: [0,1]
