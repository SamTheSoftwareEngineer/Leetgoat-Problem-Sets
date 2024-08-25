"""Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

"""
# Tags: Prefix sums 

class Solution:
    def pivotIndex(self, nums):
        # By getting the total sum, we can derive the postfix by subtracting
        # the total sum and the prefix sum
        total = sum(nums)
        print(total)  # This prints the total sum of the array, mainly for debugging purposes
        
        # We start with our leftSum as 0 since there is nothing to the left of our first
        # item in the array
        leftSum = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # The right sum will be the total - the element we are on - leftSum
            rightSum = total - nums[i] - leftSum
            
            # Check if the left sum equals the right sum
            if leftSum == rightSum:
                return i
            
            # Update the left sum by adding the current element
            leftSum += nums[i]
        
        # If no pivot index is found, return -1
        return -1 

    

