def combosum(target, nums, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return 1
    if target < 0:
        return 0
    result = 0
    for i in nums:
        result += combosum(target-i,nums,memo)
    memo[target] = result
    return result