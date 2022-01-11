def solution(skill, skill_trees):
    count = 0
    for s in skill_trees :
        stack = []
        for i in s :
            if i in skill :
                if i == skill[0] :
                    if len(stack) == 0 :
                        stack.append(i)
                    else :
                        break
                else :
                    stack.append(i)
                    idx = skill.index(i)
                    if list(skill[:idx+1]) != stack :
                        break
        else :
            count += 1
    
    return count