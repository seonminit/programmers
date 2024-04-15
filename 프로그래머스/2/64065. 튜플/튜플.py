def solution(s):
    answer = []

    s = s.replace('{', '[')
    s = s.replace('}', ']')
    s = s.replace(',[', '[')

    initial = []
    initial_dict = {}
    for item in s[1:-1]:
        if item == '[':
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
            initial_dict[len(check)] = check
            target_str = ''
    
    for i in range(1, len(initial_dict.keys())+1):
        for value in initial_dict[i]:
            if not (value in answer):
                answer.extend([value])
            else:
                pass

    return answer