def solution(id_list, report, k):
    answer = [0]*len(id_list)

    print(answer)
    dict_report = {id : [] for id in id_list}
    dict_k = {id : 0 for id in id_list}
    
    report = list(set(report))
    for re in report:
        id, value = re.split(' ')    
        dict_report[id].append(value)
        dict_k[value] += 1

    target_list = []
    
    for target in dict_k:
        if dict_k[target] >= k:
            target_list.append(target)
            
    idx= -1
    for id in id_list:
        idx +=1 
        for sub_id in dict_report[id]:
            if len(target_list) == 0:
                break
            elif sub_id in target_list:
                answer[idx] +=1 
            else:
                pass
    return answer