string_a = "Hello World!"


def remove_excl_point_from_end_of_str(x):
    return x[0:-1] if x.endswith("!") else x


print(remove_excl_point_from_end_of_str(string_a))


 # Palindrome
def palindrome(w1,w2):
    return w1 == w2[::-1]


print(palindrome('hello', 'olleh'))


def anagram(w1,w2):
    if len(w1) == len(w2):
        if sorted(w1) == sorted(w2):
            return f"The word {w1} and word {w2} are anagrams."
    return "Words are not anagrams"


def anagram2(w1,w2):
    letters_w1 = list(w1)
    print(letters_w1)
    for l2 in w2:
        if l2 in letters_w1:
            letters_w1.remove(l2)
        else:
            letters_w1.append(l2)
    return len(letters_w1) == 0


w1 = "kayaks"
w2 = 'kayak'
print("Anagram2:")
print(anagram(w1, w2))
print(anagram2(w1, w2))


def remove_first_last(x):
    return x[1:-1]


print(remove_first_last(string_a))

strs = ["flower", "flow", "flight"]


def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ''
    shortest = min(strs, key=len)  # shortest: 'flow'
    for i in range(len(shortest)):
        if sum(1 for w in strs if shortest[i] != w[i]) > 0:
            return shortest[:i]

    return shortest


print(longest_common_prefix(strs=strs))


nums = [2, 7, 5, 2]
target = 9


# triplet that gives the sum of 0
def three_sum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    length = len(nums)
    for i in range(length - 2):

        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i+1
        r = length - 1

        while l < r:
            total = nums[i]+nums[l]+nums[r]
            if total < 0:
                #-2,-1,0,1
                l = l+1
            elif total > 0:
                r = r-1

            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l = l+1
                while l < r and nums[r] == nums[r-1]:
                    r = r-1

                l = l+1
                r = r-1
    return res


three_nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(three_nums))


def two_sum(nums: list[int], target: int) -> list[int]:
    complementmap = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if num in complementmap:
            return [complementmap[num], i]
        else:
            complementmap[complement] = i


print(two_sum(nums, target))

new_str = " Hey I am here for you    "
result = ""
no = "eyi' '"
for l in new_str.lower():
    if l not in no:
        result += l

print(result.capitalize())
print(new_str.strip().count("ey"))
a = new_str.split(" ")
print(" ".join(l for l in a if l != "am"))


'''
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.
'''


def max_area(height: list[int]) -> int:
    l, r, area = 0, len(height) - 1, 0
    while l < r:
        area = max(area, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return area


height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))












