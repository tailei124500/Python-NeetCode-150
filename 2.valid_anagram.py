# quiz: Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other,
#   --> otherwise return false.
# An anagram is a string that contains the exact same characters as another string,
#   --> but the order of the characters can be different.

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

# Constraints:
# s and t consist of lowercase English letters.

# ----------------------------------------------------------------------------------------------------
# main code
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

# ----------------------------------------------------------------------------------------------------
# main code本機測試
class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

sol = Solution()
print(sol.isAnagram("racecar", "carrace"))
print(sol.isAnagram("jar", "jam"))        

# ----------------------------------------------------------------------------------------------------
# 手動測試
# Example 1:
s, t = "racecar", "carrace"
s_chars, t_chars = list(s), list(t)

# sort()函式用於排序list，用法為list.sort(reverse=True|False, key=myFunc)
#   --> reverse參數決定順序是否顛倒；key參數可加入自定義函式，自定排序順序
# e.g. 
# def myFunc(e):
#   return len(e)
# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
# cars.sort(reverse=True, key=myFunc)
# print(cars)
# 會得到['Mitsubishi', 'Ford'', 'BMW', 'VW']
print(s_chars)
s_chars.sort()
print(s_chars)

print(t_chars)
t_chars.sort()
print(t_chars)

# 備註:
# print(t_chars.sort())會印出None，chars雖被排序過，但sort()沒有回傳值
# 正確用法有兩種：
# 1. 先排序，再印出
#   --> chars.sort()
#   --> print(chars)
# 2. 使用sorted()產生新list
#   --> chars = ['w', 's', 'd', 'a']
#   --> print(sorted(chars))
# 使用sorted()須注意! 原本的chars沒有被改變

print(s_chars == t_chars)

# Example 2: 
# 改使用sorted()
s, t = "jar", "jam"
s_chars, t_chars = list(s), list(t)

print(s_chars)
print(sorted(s_chars))

print(t_chars)
print(sorted(t_chars))

print(s_chars == t_chars)