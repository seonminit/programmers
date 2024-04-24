def solution(record):
    answer = []
    
    # setting_user
    user_dict = {}
    
    answer_record = []
    
    for rec in record:
        split_rec = rec.split(' ')
        if split_rec[0] in ['Enter', 'Leave']:
            answer_record.append(rec)
        # setting_user
        if split_rec[0] == 'Leave':
            continue
        else:
            user_dict[split_rec[1]] = split_rec[2]
    
    for rec in answer_record:
        rec_split = rec.split(' ')
        if rec_split[0] == 'Enter':
            answer.append(f'{user_dict[rec_split[1]]}님이 들어왔습니다.')
        else: 
            answer.append(f'{user_dict[rec_split[1]]}님이 나갔습니다.')
    return answer