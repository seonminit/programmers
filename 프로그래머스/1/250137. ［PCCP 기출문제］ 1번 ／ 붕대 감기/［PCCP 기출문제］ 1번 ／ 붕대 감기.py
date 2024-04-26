def solution(bandage, health, attacks):
    answer = health
    attack_i = [t[0] for t in attacks]
    success = 0
    for i in range(attacks[-1][0]+1):
        if i == 0: continue
        
        elif i in attack_i:
            index = attack_i.index(i)
            dam = attacks[index][1]
            success = 0
            if answer > health:
                answer = health
                answer -= dam
            else:
                answer -= dam
            if answer <= 0:
                return -1
        else:
            success += 1
            if answer < health:
                answer += bandage[1]

            if (success == bandage[0]) & (answer < health):
                answer += bandage[-1]
                success = 0
                
            if answer > health:
                answer = health
    if answer <= 0:
        answer = -1
            
    return answer