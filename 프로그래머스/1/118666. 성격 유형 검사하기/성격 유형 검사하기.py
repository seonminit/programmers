def solution(survey, choices):
    answer = ''
    score = [3,2,1,0,1,2,3]
    label = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    answer_dict = {l: 0 for l in label}
    
    for idx, sur in enumerate(survey):
        if choices[idx] <= 3:
            target_s = sur[0]
        elif choices[idx] >= 5:
            target_s = sur[1]
        else:
            continue
        
        target_score = score[choices[idx]-1]
        answer_dict[target_s] += target_score
        
    label_a = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    for a in label_a:
        if answer_dict[a[0]] < answer_dict[a[1]]:
            answer += a[1]
        else:
            answer += a[0]
    return answer