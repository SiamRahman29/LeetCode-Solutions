def solution(target, nums):
    for i in range(len(nums)):
        if (target - nums[i]) in nums[i+1:]:
            a = i
            b = nums[i+1:].index(target - nums[i]) + i + 1
            return([a,b])