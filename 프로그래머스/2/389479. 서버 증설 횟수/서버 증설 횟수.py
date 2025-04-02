def solution(players, m, k):
    answer = 0
    server_list = [0]*24

    for idx in range(len(players)):
        player = players[idx]
        check = player // m
        if check == 0:
            continue
        elif (check >= 1) and (check <= server_list[idx]):
            continue
        elif (check >= 1) and (check > server_list[idx]):
            target_add = check - server_list[idx]
            answer += target_add
            for i in range(k):     
                if idx+i < 24:
                    server_list[idx+i] += target_add
                else: 
                    break     
            
    return answer