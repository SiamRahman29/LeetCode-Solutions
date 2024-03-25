def isPalindrome(self, s: str) -> bool:
    l = []
    s = s.lower()

    for i in s:
        if i.isalnum():
            l.append(i)
            
    g = l.copy()
    g.reverse()
    
    if l == g:
        return True
    else:
        return False
