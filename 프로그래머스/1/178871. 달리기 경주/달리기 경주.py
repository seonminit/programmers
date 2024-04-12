def solution(players, callings):
    answer = players

    dict = {}
    for idx, play in enumerate(players):
        dict[play] = idx
        
    for call in callings:
        index = dict[call]  
        front_call = answer[index-1]
        answer[index-1] = call
        answer[index] = front_call

        dict[call] = index-1
        dict[front_call] = index
        
    return answer