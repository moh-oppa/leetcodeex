bruteforce
def removeElement(nums: List[int], val: int) -> int:
    i= 0
    j= 0
    k = len(nums)
    popped_num=[]
    if k == 0:
        return("Empty list")

    while i < k:
        if val == nums[i]:
            popped_num = nums.pop(i)
            j+=1
        else:
            i+=1


    nums.extend(popped_num)
    return i





def removeElement(nums: List[int], val: int) -> int:
    i = 0
    removed_elements = []

    while i < len(nums):
        if nums[i] == val:
            removed_elements.append(nums.pop(i))
        else:
            i += 1

    nums.extend(removed_elements)

    return i


print(removeElement([], 3))
