def solution(nums):
    result = []
    prefix = []
    postfix = []
    pre = 1
    for i in nums:
        pre = pre*i
        prefix.append(pre)
    post = 1
    for i in nums[::-1]:
        post = post*i
        postfix.append(post)
    postfix.reverse()
        #print(prefix)
        #print(postfix)
    for i in range(len(nums)):
        if i == 0:
            result.append(postfix[i+1])
        elif i == len(nums) - 1:
            result.append(prefix[i-1])
        else:
            result.append(prefix[i-1]*postfix[i+1]) 
    return(result)
