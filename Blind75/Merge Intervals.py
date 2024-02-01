def merge(intervals):
    res = []

    intervals.sort()

    curr = intervals[0]
    def add(a,b):
        return [min([a[0],b[0]]),max([a[1],b[1]])]
    
    for i in range(1,len(intervals)):
        if curr[1] >= intervals[i][0]:
            curr = add(curr,intervals[i])
        else:
            res.append(curr)
            curr = intervals[i]
        
    res.append(curr)
    return res
