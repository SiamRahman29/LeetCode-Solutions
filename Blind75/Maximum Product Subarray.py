def solution(nums):
    currMin = 1
    currMax = 1
    result = max(nums)
    for i in nums:
        t = currMax*i
        currMax = max([i, currMax*i, currMin*i])
        currMin = min([i, t, currMin*i])
        result = max([result,currMax])
    return result