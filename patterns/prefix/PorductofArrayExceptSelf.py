# Problem: 
"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

"""


# Tags: prefix 


"""Suppose the input array nums is [1, 2, 3, 4].

Initial Setup:
nums = [1, 2, 3, 4]
answer = [1, 1, 1, 1]  # Initialized with 1s


Step-by-Step Process:
Step 1: Calculate Prefix Products

We will iterate through nums from left to right and fill the answer array with the prefix products.

Initialization:

prefix = 1

Iteration:

for i in range(len(nums)):
    answer[i] = prefix
    prefix *= nums[i]

i = 0:

answer[0] = prefix  # answer[0] = 1
prefix *= nums[0]   # prefix = 1 * 1 = 1
Updated answer array: [1, 1, 1, 1]

i = 1:

answer[1] = prefix  # answer[1] = 1
prefix *= nums[1]   # prefix = 1 * 2 = 2
Updated answer array: [1, 1, 1, 1]

i = 2:

answer[2] = prefix  # answer[2] = 2
prefix *= nums[2]   # prefix = 2 * 3 = 6
Updated answer array: [1, 1, 2, 1]

i = 3:

answer[3] = prefix  # answer[3] = 6
prefix *= nums[3]   # prefix = 6 * 4 = 24
Updated answer array: [1, 1, 2, 6]

At this point, the answer array contains the prefix products up to each index.

Step 2: Calculate Postfix Products

We will iterate through nums from right to left and multiply the existing values in the answer array by the postfix products.

Initialization:

postfix = 1

Iteration:

for i in range(len(nums) - 1, -1, -1):
    answer[i] *= postfix
    postfix *= nums[i]
i = 3:

answer[3] *= postfix  # answer[3] = 6 * 1 = 6
postfix *= nums[3]    # postfix = 1 * 4 = 4
Updated answer array: [1, 1, 2, 6]

i = 2:

answer[2] *= postfix  # answer[2] = 2 * 4 = 8
postfix *= nums[2]    # postfix = 4 * 3 = 12
Updated answer array: [1, 1, 8, 6]

i = 1:

answer[1] *= postfix  # answer[1] = 1 * 12 = 12
postfix *= nums[1]    # postfix = 12 * 2 = 24

Updated answer array: [1, 12, 8, 6]

i = 0:
answer[0] *= postfix  # answer[0] = 1 * 24 = 24
postfix *= nums[0]    # postfix = 24 * 1 = 24 (no change since nums[0] is 1)

Updated answer array: [24, 12, 8, 6]

At this point, the answer array contains the product of all elements in nums except for the element at each index.

Final Result
The final answer array is [24, 12, 8, 6].
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        answer = [1] * (len(nums))
        prefix = 1 

        # Filling answer array with prefix values
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Fill answer array with postfix values
        postfix = 1
        for i in range(len(nums) -1, -1, -1,):
            answer[i] *= postfix 
            postfix *= nums[i]

        return answer

