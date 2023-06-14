# The "B means that this is a brute force slution
def threeSumB(nums: list[int]) -> list[list[int]]:
    final = []
    for i in range(len(nums) - 2):
        level_one = nums[i + 1:]
        for j in range(len(level_one) - 1):
            level_two = nums[i+1:][j+1:]
            for k in range(len(level_two)):
                if nums[i] + level_one[j] + level_two[k] == 0:
                    arr = [nums[i],level_one[j],level_two[k]]
                    arr.sort()
                    if arr not in final:
                        final.append(arr)
    return(final) 

#print(threeSumB([1,0,2,-1,4,3,-2])) #Gives the correct answer but brute force

def threeSum(nums: list[int]) -> list[list[int]]:
    
    finals = []

    
    
    nums.sort()

    #print(nums)
    left = 0
    right = len(nums)-1
    while(left < right):
        third = -(nums[left] + nums[right]) 
        #print(nums[left], third, nums[right])
        #print(nums[left+1:right])
        if third in nums[left:right]:
            arr = [nums[left],third,nums[right]]
            c_arr = list(set(arr))
            c_arr.sort()
            if arr == c_arr:
                finals.append(arr)
        if -third > 0:
            right -= 1
        else:
            left += 1
    return finals
# -2, -1, 0, 1, 2, 3, 4
print(threeSumB([-1,0,1,2,-1,-4]))
print(threeSum([-1,0,1,2,-1,-4]))

