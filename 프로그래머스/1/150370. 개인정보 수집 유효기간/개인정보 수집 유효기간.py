def solution(today, terms, privacies):
    answer = []
    # today
    year, month, day = [int(item) for item in today.split('.')]

    # terms
    terms_dict = {}
    for term in terms:
        key, value = term.split(' ')
        terms_dict[key] = int(value) 
    
    # privacies
    idx = 0
    for privacy in privacies:
        idx += 1
        key = privacy[-1]
        y, m, d = [int(item) for item in privacy[:-2].split('.')]
        
        target_y = y
        target_m = m+terms_dict[key]
        target_d = d-1

        while target_m > 12:
            target_m -= 12
            target_y += 1
            
        if target_d == 0:
            target_m -= 1
            target_d = 28
        
        # check
        if year < target_y:
            continue
        elif year == target_y:
            if month < target_m:
                continue
            elif month == target_m:
                if day <= target_d:
                    continue 
                else:
                    answer.append(idx)
            else:
                answer.append(idx)       
        else:
            answer.append(idx)
            
    return answer