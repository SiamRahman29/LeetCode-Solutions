def rob(self, nums):
    cache = nums
    if len(nums) > 3:
        cache[-3] = cache[-3] + cache[-1]
        for h in range(len(nums)-4,-1,-1):
            print(h)
            cache[h] = max([cache[h] + cache[h+2],cache[h] + cache[h+3]])
            print(cache)
    elif len(nums) == 3:
        return(max([nums[0]+nums[2],nums[1]]))
    elif len(nums) == 2:
        return max(nums)
    else:
        return nums[0]        
    return max(cache)