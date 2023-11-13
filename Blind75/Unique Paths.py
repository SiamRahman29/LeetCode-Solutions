def solve(m,n,memo={}):
    result = 0
    if m == 1 and n == 1:
        print("ADD " + str(result))
        return 1
    if m < 1 or n < 1:
        return 0
    if (m,n) in memo:
        return memo[(m,n)]

    
    print((m,n))
    result = solve(m-1,n,memo) + solve(m,n-1,memo)
    memo[(m,n)] = result
    return memo[(m,n)]