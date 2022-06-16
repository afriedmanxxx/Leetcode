import collections
from typing import List

# ************    BLIND TOP 100 QUESTIONS   **************

# https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-100-LeetCode-Questions-to-Save-Your-Time-OaM1orEU

# Most common
# Anagram
class Words:
    w1 = "kayak"
    w2 = "kayak"

    def anagram(self, w1, w2):
        if len(w1.strip()) != len(w2.strip()):
            return False
        letters_w1 = list(w1)
        for l in w2:
            if l in letters_w1:
                letters_w1.remove(l)
            else:
                letters_w1.append(l)
        return len(letters_w1) == 0


# Palindrome
    def polindrome(self, w1):
        return w1 == w1[::-1]


check = Words()
print(check.anagram("work", "wokk"))

# Common prefix
words = ["coor", "cooler", "cool", "coopper"]


def common_prefix(words):
    smallest_word = min(words, key=len)
    for i in range(len(smallest_word)):
        if sum(1 for w in words if smallest_word[i] != w[i]) > 0:
            return smallest_word[:i]
    return smallest_word


print(common_prefix(words))

dups = [6, 4, 5, 5, 2]


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


dups_subj = Solution()
print(dups_subj.contains_duplicate(dups))

# Quick sort
def quick_sort(n):
    if len(n) <= 1:
        return n
    else:
        pivot = n.pop()

    smaller = [x for x in n if x < pivot]
    bigger = [x for x in n if x > pivot]

    return quick_sort(smaller) + [pivot] + quick_sort(bigger)


print(quick_sort(dups))


# ****************** Array LIST **********************
# 1 Twosum
nums = [2, 7, 11, 15, 11]
target = 9


def twoSum(nums, target):
    complementmap = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num  # 7
        if num in complementmap:
            return [complementmap[num], i]
        else:
            complementmap[complement] = i


print("THe two sum is: \t", twoSum(nums, target))

# 2 Max Profit
prices = [7, 1, 5, 3, 6, 4]


class Solution:
    def max_profit(self, prices):
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            current_profit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(max_profit, current_profit)
            else:
                left = right
            right += 1
        return max_profit


a = Solution()
print("My profit is \t" + f"{a.max_profit(prices)}!")





# 3 return Max sub array of sum [1,2,3 -1, -3, 3] -> 6
def max_sub_array(nums: List[int]) -> int:
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)

dups = [6, 4, 5, -100, 30, 2,-100, 8]
print(max_sub_array(dups))


#4 Maximum Product Subarray
def maxProduct(nums):
    max_prod, min_prod, ans = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        x = max(nums[i], max_prod * nums[i], min_prod * nums[i])
        y = min(nums[i], max_prod * nums[i], min_prod * nums[i])
        max_prod, min_prod = x, y
        ans = max(max_prod, ans)
    return ans

max_prod = [2,3,-2,4]
print(maxProduct(max_prod))


# ******************** String *******************
# 1
def lengthOfLongestSubstring(s):
    used = {}
    max_length = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used[c] = i

    return max_length

s = "abcabcbb"
print(lengthOfLongestSubstring(s))


# 2  Longest Repeating Character Replacement
s = "AABABBA"
k = 1  # how many times we can change character to the one we need to extend the pattern.

def characterReplacement(s, k):
    maxf = i = 0
    count = collections.Counter()
    for j in range(len(s)):
        count[s[j]] += 1
        maxf = max(maxf, count[s[j]])
        if j - i + 1 > maxf + k:
            count[s[i]] -= 1
            i += 1
    return len(s) - i

# 3 Minimum window that has all the characters t in str s:
'''
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' 
from string t.
'''
def min_window(s, t):
    need, missing = collections.Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
    return s[I:J]


s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))


print("$"*200)

