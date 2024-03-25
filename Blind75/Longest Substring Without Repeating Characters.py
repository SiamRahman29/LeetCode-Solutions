def lengthOfLongestSubstring(s):
    res = 0
    for i in range(len(s)):
        l, r = i, i
        passed = []
        while r < len(s) and s[r] not in passed:
            passed.append(s[r])
            if (r - l + 1) > res:
                #print(l, r)
                res = r - l + 1
            r += 1
    return res
