def courseSchedule(numCourses, prerequisites):
    hashMap = {}
    for num in range(numCourses):
        hashMap[num] = []
    for pair in prerequisites:
        if pair[0] in hashMap:
            hashMap[pair[0]].append(pair[1])
        else:
            hashmap[pair[0]] = pair[1] 
    
    starters = []
    result = False
    for course in hashMap:
        if hashMap[course] == []:
            starters.append(course)
    for starter in starters:
        del hashMap[starter]
    while(len(starters) != 0):
        if hashMap == {}:
            result = True
            break
        checker = starters[0]
        for course in hashMap:
            if checker in hashMap[course]:
                hashMap[course].remove(checker)
            if hashMap[course] == []:
                starters.append(course)
                     
        starters.remove(checker)
        for starter in starters:
            if starter in hashMap:
                del hashMap[starter]

    return result
        
