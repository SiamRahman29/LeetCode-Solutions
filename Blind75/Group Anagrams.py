def groupAnagrams(strs):
    strs_copy = strs.copy()
    res = []
    for i in range(len(strs)):
        strs[i] = "".join(sorted(strs[i]))
    for i in range(len(strs)):
        sub_res = []
        for j in range(len(strs)):
            if strs[i] == strs[j]:
                sub_res.append(strs_copy[j])
        res.append(sub_res)
    res_f = []
    [res_f.append(x) for x in res if x not in res_f]
    return res_f