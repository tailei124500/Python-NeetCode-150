# quiz: Valid Palindrome
# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. 
#   --> It is also case-insensitive and ignores all non-alphanumeric characters.
# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Example 1:
# Input: s = "Was it a car or a cat I saw?"
# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:
# Input: s = "tab a cat"
# Output: false
# Explanation: "tabacat" is not a palindrome.

# Constraints:
# 1 <= s.length <= 1000
# s is made up of only printable ASCII characters.

# ----------------------------------------------------------------------------------------------------
# main code
# class Solution:
#     def isPalindrome(self, s: str) -> bool:

# ----------------------------------------------------------------------------------------------------
# main code本機測試
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.replace("?", "")
        # s = s.replace(",", "")
        # s = s.replace("'", "")
        # s = s.replace(".", "")
        # s = s.replace(" ", "")
        # 以上方法需要replace()多次才能替代掉所有不需要的標點符號，效率差
        #   --> 可改用isalnum()函式
        s = s.lower()
        filter_s = []

        for i in s:
            if i.isalnum():
                filter_s.append(i)

        print(filter_s)

        output = []

        for j in range(len(filter_s)):
            if filter_s[j] == filter_s[-(j+1)]:
                # 將轉成list的純大小寫英文字母、數字進行前後比對，比對的結果(bool)全部加進一個新的list中
                output.append(True)
            else:
                output.append(False)

        return all(output) # 使用all()函式判斷將裝有多個bool的List，只要有含False，一律return False，反之return True
    
sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?"))
print(sol.isPalindrome("tab a cat"))

# ----------------------------------------------------------------------------------------------------
# isalnum()函式練習
# isalnum()用於檢查字元是不是字母或數字
s = "Was it a car or a cat I saw?"
s = s.lower()
filter_s = []

for i in s:
    if i.isalnum():
        filter_s.append(i)
# 以上可使用生成式寫法: 「filter_s = [i for i in s if i.isalnum()]」

print(filter_s)

# ----------------------------------------------------------------------------------------------------
# 手動測試
# Example 1:
s = "Was it a car or a cat I saw?"
s = s.replace("?", "")
s = s.replace(" ", "")
s = s.lower()
s = list(s)
print(s)

for i in range(len(s)):
    if s[i] == s[-(i+1)]:
        print(True)
    else:
        print(False)

# Example 2: 
# 改善Example 1中for迴圈每次皆印出bool的問題，將跑出來bool加進一個新的list
#   --> 最後用all()函式判斷將裝有多個bool的List，只要有含False，一律印出False，反之印出True
s = "tab a cat"
s = s.replace(" ", "")
s = list(s)
print(s)

output = []

for j in range(len(s)):
    if s[j] == s[-(j+1)]:
        output.append(True)
    else:
        output.append(False)

print(all(output))

# ----------------------------------------------------------------------------------------------------
# 最佳解本機測試
# 最佳解使用join() + 生成式一次建立乾淨的小寫字串
#   --> 直接用字串反轉語法[::-1]判斷是否回文，省掉整個迴圈比對的過程
# 最佳解與main code本機測試兩者效能差不多，都是O(n)
# 精簡版的可讀性更高，也更貼近Python常見的寫法

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 建立只含有字母與數字的小寫字串
        filtered = "".join(ch.lower() for ch in s if ch.isalnum())
        
        # 比對正序與反序是否相同
        return filtered == filtered[::-1]

sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?"))
print(sol.isPalindrome("tab a cat"))