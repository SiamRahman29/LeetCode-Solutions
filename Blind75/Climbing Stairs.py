def find(num, memo = {}):
    if num in memo:
        return memo[num]
    if num == 1:
        return 1
    if num == 2:
        return 2
    memo[num] = find(num-1,memo) + find(num-2,memo)
    return memo[num]
