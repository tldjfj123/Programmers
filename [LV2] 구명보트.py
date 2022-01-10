def solution(people, limit):
    people.sort()
    s = 0
    e = len(people) - 1
    boat = 0
    while s <= e :
        boat += 1
        if people[s] + people[e] <= limit :
            s += 1
        e -= 1
            
    return boat