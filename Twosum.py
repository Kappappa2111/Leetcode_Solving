class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []

# Input
nums = input("Enter a list of numbers (e.g., [2, 7, 11, 15]): ")
target = int(input("Enter an integer target: "))

nums = eval(nums)

solution = Solution()
result = solution.twoSum(nums, target)

print("Indices of the two numbers that add up to target:", result)
