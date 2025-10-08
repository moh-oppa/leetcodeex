# from typing import List


# # Bruteforce
# def two_sum(nums: List[int], target: int) -> List[int]:
#     if len(nums) < 2:
#         return "Empty list or not enough values"

#     firstvalue = 0
#     secondvalue = len(nums) - 1
#     while firstvalue < secondvalue:
#         if nums[firstvalue] + nums[secondvalue] == target:
#             return [firstvalue, secondvalue]
#         elif nums[firstvalue] + nums[secondvalue] < target:
#             firstvalue += 1
#         else:
#             secondvalue -= 1
#     return "Not Found"


# # Revised
# def two_sum(nums: List[int], target: int) -> List[int]:
#     index_map = {}

#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in index_map:
#             return [index_map[complement], i]
#         index_map[num] = i

#     return "Not Found"


# new = [2]
# target = 18
# result = two_sum(new, target)
# print(result)


# # bruteforce
# def isPalindrome(x: int) -> bool:
#     if x < 0:
#         return False

#     num0 = x
#     L = 0
#     num1 = []

#     while L != len(str(num0)):
#         values = (num0 // 10 ** L) % 10
#         num1.append(values)
#         L += 1

#     num2 = list(reversed(num1))
#     return num1 == num2


# # revised
# def isPalindrome(x: int) -> bool:
#     if x < 0:
#         return False  # Negative numbers are not palindromes

#     original = x
#     reversed_num = 0

#     while x > 0:
#         reversed_num = reversed_num * 10 + x % 10
#         x //= 10

#     return original == reversed_num


# # Example usage:
# print(isPalindrome(121))  # Output: True
# print(isPalindrome(-121))  # Output: False
# print(isPalindrome(10))  # Output: False

# # bruteforce
# # class Solution:
# # def removeElement(nums: List[int], val: int) -> int:
# #     i= 0
# #     j= 0
# #     k = len(nums)
# #     popped_num=[]
# #     if k == 0:
# #         return("Empty list")

# #     while i < k:
# #         if val == nums[i]:
# #             popped_num = nums.pop(i)
# #             j+=1
# #         else:
# #             i+=1


# #     nums.extend(popped_num)
# #     return i


# def removeElement(nums: List[int], val: int) -> int:
#     i = 0
#     removed_elements = []

#     while i < len(nums):
#         if nums[i] == val:
#             removed_elements.append(nums.pop(i))
#         else:
#             i += 1

#     nums.extend(removed_elements)

#     return i


# print(removeElement([], 3))


def strStr(haystack: str, needle: str) -> int:
    # h = list(haystack)
    # n = list(needle)
    i = 0
    start = -1
    stop = -1

    while i < len(needle): #True
        for x, y in enumerate(haystack): #x=2 y= r
            if i == len(needle):
                break
            if y == needle[i]:
                if start == -1:
                    start = x
                stop = x
                i += 1 #i=1
            
        break
    if stop - start + 1 == len(needle):
        return x - len(needle)
    elif i == 0:
        return -1
    else:
        return -1


result = strStr("kouhredemuhammed", "uha")
print(result)

# # gpt
# def strStr(haystack: str, needle: str) -> int:
#     # Convert both strings to lists
#     h = list(haystack)
#     n = list(needle)

#     # Handle edge case where needle is an empty string
#     if not n:
#         return 0

#     h_len = len(h)
#     n_len = len(n)

#     # Iterate through haystack, checking possible starting positions
#     for i in range(h_len - n_len + 1):
#         # Check if the sublist from i matches the needle
#         if h[i:i + n_len] == n:
#             return i  # Found match, return starting index

#     # If no match is found, return -1
#     return -1

def roman(numeral: str)-> int:
    roman = {"I": 1, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
