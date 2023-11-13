def solution(nums, target):
    l = 0
    r = len(nums)-1
    memo = {}
    result = -1
    found = False
    for i in range(len(nums)):
        memo[nums[i]] = i
    nums.sort()
    print(nums)
    while(l<=r):
        m = (l+r)//2
            
        if nums[m] == target:
            found = True
            break
        elif nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
    if(found):
        result = memo[target]
    return result 