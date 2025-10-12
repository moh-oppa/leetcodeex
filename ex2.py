from typing import List


def removeDuplicates(nums: List[int]) -> int:
    fv = 1
    nv = 1

    if len(nums) > 1:
        while nv < len(nums):
            if nums[nv] != nums[nv - 1]:
                nums[fv] = nums[nv]
                fv += 1
            nv += 1

        return fv

    elif len(nums) == 1:
        return 1

    else:
        print("List is empty")
        return 0


print(removeDuplicates([1, 1, 1, 2, 2, 3, 3, 4]))
