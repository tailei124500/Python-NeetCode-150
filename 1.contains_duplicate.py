# quiz: Contains Duplicate
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true

# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

# ----------------------------------------------------------------------------------------------------
# main code
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:

# ----------------------------------------------------------------------------------------------------
# main code本機測試
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
    # 「nums: List[int]」並非賦值，而是告知nums為一個整數的清單，屬於「型別提示」，不會影響程式執行，也可刪除
    # 「-> bool」不是運算符號，而是表示該函式會回傳bool(True or False)，一樣屬於「型別提示」
        return len(set(nums)) != len(nums) # 「!=」其意思為不等於
    
sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 3]))
print(sol.containsDuplicate([1, 2, 3, 4]))

# ----------------------------------------------------------------------------------------------------
# main code本機測試(刪除「型別提示」)
class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)
    
sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 3]))
print(sol.containsDuplicate([1, 2, 3, 4]))

# ----------------------------------------------------------------------------------------------------
# 手動測試
nums1 = [1, 2, 3, 3]

if len(set(nums1)) == len(nums1):
    print(False)
else:
    print(True)

nums2 = [1, 2, 3, 4]

if len(set(nums2)) == len(nums2):
    print(False)
else:
    print(True)