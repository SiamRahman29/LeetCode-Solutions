def rob(nums):
    if len(nums) < 4:
        return max(nums)
    cache1 = nums[1::]
    cache2 = nums[:len(nums)-1:]
    print(cache2)
    
    if len(cache1) > 3:
        cache1[-3] = cache1[-3] + cache1[-1]
        cache2[-3] = cache2[-3] + cache2[-1]
        for h in range(len(cache1)-4,-1,-1):
            #print(h)
            cache1[h] = max([cache1[h] + cache1[h+2],cache1[h] + cache1[h+3]])
            cache2[h] = max([cache2[h] + cache2[h+2],cache2[h] + cache2[h+3]])
            #print(cache1)
        
    else:
        return max([max([cache1[0]+cache1[2],cache1[1]]),max([cache2[0]+cache2[2],cache2[1]])])
            
    return max([max(cache1),max(cache2)])