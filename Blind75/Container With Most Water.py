def solution(height):
    maxArea = 0
    left = 0
    right = len(height) - 1
    while right > left:
        maxArea = max([maxArea,min([height[left],height[right]])*(right-left)])
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return maxArea
