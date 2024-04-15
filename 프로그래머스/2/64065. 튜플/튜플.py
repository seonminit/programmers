def solution(s):
    answer = []

    s = s.replace('{', '[')
    s = s.replace('}', ']')
    s = s.replace(',[', '[')
    print(s)
    initial = []
    initial_dict = {}
    idx = -1
    for item in s[1:-1]:
        if item == '[':
            idx +=1 
            check = []
            target_str = ''
        elif (item != ',' and item != "]"):
            target_str += item
        elif item == ',':
            check.append(int(target_str))
            target_str = ''
        elif item == ']':
            check.append(int(target_str))
            initial.append(check)
            initial_dict[idx] = len(check)
            target_str = ''
            
    print(initial)
    print(initial_dict)
    return answer