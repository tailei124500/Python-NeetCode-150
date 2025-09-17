# quiz: Two Sum
# Given an array of integers nums and an integer target,
#   --> return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#   --> Return the answer with the smaller index first.

# Example 1:
# Input: 
# nums = [3,4,5,6], target = 7
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:
# Input: nums = [4,5,6], target = 10
# Output: [0,2]

# Example 3:
# Input: nums = [5,5], target = 10
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000

# ----------------------------------------------------------------------------------------------------
# main code
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

# ----------------------------------------------------------------------------------------------------
# main code本機測試
class Solution:
    def twoSum(self, nums: list[int], target: int) ->list[int]:
        # 答案需參考下方手動測試的Example 3形式，其理由如Example 3註解所述
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return sorted([i, j])

sol = Solution()
print(sol.twoSum([3, 4, 5, 6], 7))
print(sol.twoSum([4, 5, 6], 10))
print(sol.twoSum([5, 5], 10))

# ----------------------------------------------------------------------------------------------------
# 手動測試
# Example 1:
nums, target = [3, 4, 5, 6], 7
output = []

for i in nums:
    for j in nums:
        if i + j == target and i != j:
            output = sorted([nums.index(i), nums.index(j)])
            
print(output)

# Example 2:
nums, target = [4, 5, 6], 10
output = []

for k in nums:
    for l in nums:
        if k + l == target and k != l:
            output = sorted([nums.index(k), nums.index(l)])
            
print(output)

# Example 3:
nums, target = [5, 5], 10
output = []

# Example 3無法使用上方Example 1/2的直接走過nums再判斷nums的value互相相加等於target的結果
#   --> 因為for走過的value都是5，程式會重複抓到同個index的5，導致output抓不出值
#   --> 故須改用for走過nums index的方式，來取得對應value相加後會等於target的index，再組成新的list
#   --> 改用for走過nums index主要是因為list的value有可能相同，但index一定不同，走過index較不會出錯
for m in range(len(nums)):
    # print(f"m:{m}")
    for n in range(len(nums)):
        # print(f"n:{n}")
        if nums[m] + nums[n] == target and m != n:
            output = sorted([m, n])

print(output)

# ----------------------------------------------------------------------------------------------------
# 最佳解本機測試

# 改良後的解法只用一層迴圈，僅用O(n)時間就解決
#   --> seen字典記錄「這個數字出現過，索引是多少」
#   --> 每遇到一個數字，就馬上檢查「另一半complement是否已經出現過」
#   --> 一旦找到就回傳結果

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # 用來記錄 {數字: 索引}
        
        for i, num in enumerate(nums):
            complement = target - num  # 我需要的另一個數
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9)) # [0, 1]
print(sol.twoSum([3, 2, 4], 6)) # [1, 2]
print(sol.twoSum([3, 3], 6)) # [0, 1]