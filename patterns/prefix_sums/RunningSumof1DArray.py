# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.
# Example 1:

# Tag: prefix 

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].



def runningSum(nums): 
    answer = []
    running_sum = 0
    for num in nums:
        running_sum += num
        answer.append(running_sum)
    return answer