def solution(s, wordDict):
    memo = {}
    if s == "":
        return True
    if s in memo:
        return True
    for word in wordDict:
        if s.startswith(word):
            s_copy = s[len(word)::]
            if solution(s_copy, wordDict):
                memo[s] = True
                return memo[s]
            
    memo[s] = False         
    return memo[s]