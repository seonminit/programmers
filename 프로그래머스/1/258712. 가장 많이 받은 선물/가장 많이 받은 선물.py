def solution(friends, gifts):
    history_present = [[0] * len(friends) for _ in friends]

    gift_jisu = [0] * len(friends)
    score_per = [0] * len(friends)

    for item in gifts:
        name = item.split(' ')
        give_per, take_per = friends.index(name[0]), friends.index(name[1])
        history_present[give_per][take_per] += 1

        gift_jisu[give_per] += 1
        gift_jisu[take_per] -= 1


    for per1 in range(len(friends)-1):
        for per2 in range(per1+1, len(friends)):
            if history_present[per1][per2] > history_present[per2][per1]:
                score_per[per1] +=1
            elif history_present[per2][per1] > history_present[per1][per2]:
                score_per[per2] +=1
            else:
                if gift_jisu[per1] > gift_jisu[per2]:
                    score_per[per1] +=1
                elif gift_jisu[per2] > gift_jisu[per1]:
                    score_per[per2] +=1 


    result = sorted(score_per)[-1]
    return result