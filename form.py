# def twosum(nums: list, target: int) -> list:
#     map = {}
#     for i, n in enumerate(nums):
#         new = target - n
#         if new in map:
#             return [map[new], i]
#         else:
#             map[n] = i

#     return False

def twosum2(nums: list, target: int) -> list:
    l, r = 0, len(nums)-1
    while l < r:
        cursum = nums[l] + nums[r]
    
        if cursum < target:
            l += 1
        elif cursum > target:
            r -= 1
        else:
            return [l+1, r+1]
        

n = [2,3,4,8,11,14,17]
target = 21
print(twosum2(n, target))
