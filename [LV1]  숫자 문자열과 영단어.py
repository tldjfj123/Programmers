def solution(s):
    table = dict()
    for i in range(10) :
        table[str(i)] = str(i)
    
    table['zero'] = '0'
    table['one'] = '1'
    table['two'] = '2'
    table['three'] = '3'
    table['four'] = '4'
    table['five'] = '5'
    table['six'] = '6'
    table['seven'] = '7'
    table['eight'] = '8'
    table['nine'] = '9'
    
    stack = []
    res = []
    
    for i in s :
        stack.append(i)
        if ''.join(stack) in table.keys() :
            res.append(table[''.join(stack)])
            stack = []
    return int(''.join(res))