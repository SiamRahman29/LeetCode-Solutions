def solution(nums):
    nums2 = list(set(nums))
    nums.sort()
    nums2.sort()
    if nums == nums2:
        return False
    else:
        return True