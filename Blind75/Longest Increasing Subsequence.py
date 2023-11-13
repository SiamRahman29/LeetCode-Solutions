def solution(nums):
    val = [1]*len(nums)
    for i in range(len(nums)-1,-1,-1):
        for j in range(i+1,len(nums)):
            if nums[i]<nums[j]:
                val[i] = max([val[i],1 + val[j]])
    return max(val)