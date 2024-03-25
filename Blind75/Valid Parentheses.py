def isValid(s):
    ends = [")","}","]"]
    stack = []
    for i in s:
        if i not in ends:
            stack.append(i)
        else:
            try:
                if i == ")":
                    if stack[-1] == "(":
                        stack.pop(-1)
                    else:
                        return False
                elif i == "}":
                    if stack[-1] == "{":
                        stack.pop(-1)
                    else:
                        return False
                else:
                    if stack[-1] == "[":
                        stack.pop(-1)
                    else:
                        return False
            except:
                return False
    if len(stack) == 0:
        return True
    else:
        return False