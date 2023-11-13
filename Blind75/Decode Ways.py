
def getCombos(s):
    
    #Split s into combos
    combos = []
    combos = [x for x in s]
    i = 0
    while(i < len(s)-1):
        a = s[i]+s[i+1]
        if int(a) <= 26:
            combos.append(a)
        i += 2
    i = 1
    while(i < len(s)-1):
        a = s[i]+s[i+1]
        if int(a) <= 26:
            combos.append(a)
        i += 2
    combos_end = []
    [combos_end.append(x) for x in combos if x not in combos_end]
    return combos_end
def memoize(s, combos, memo):
    

    result = 0
    if s == "":
    
        return 1
    if s in memo:
        return memo[s]
    

    for i in combos:
        if s.startswith(i) and i[0] != "0":
            s_copy = s[len(i)::]
            
            result += memoize(s_copy,combos,memo)
            

    memo[s] = result
    return result

def solution(s):
    memo = {}
    if s == "":
        return 0
    combos = getCombos(s)
    return memoize(s, combos, memo)