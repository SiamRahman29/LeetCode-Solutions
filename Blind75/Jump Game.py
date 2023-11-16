def canJump(nums):
    pos = 0
    for i in range(len(nums)):
        if i > pos:
            return False
        pos = max([pos, i + nums[i]])
    return True