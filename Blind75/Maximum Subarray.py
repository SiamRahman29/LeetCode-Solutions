def solution(nums):
    """
        #Brute Force Quadratic Solution
        for i in range(len(nums)):
            currSum = 0
            for j in range(i,len(nums)):
                currSum = currSum + nums[j]
                if currSum > result:
                    result = currSum

        return result
        """
    left = 0
    right = 1
    currSum = nums[left]
    result = currSum
    while(right < len(nums)):
        currSum += nums[right]
        if nums[right] > currSum:
            left = right
            currSum = nums[left]
        result = max([result, currSum])
        right += 1
    return result