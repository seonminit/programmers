def solution(park, routes):    
    park = [list(p) for p in park]

    for h in range(len(park)):
        try:
            w = park[h].index('S')
            break
        except:
            pass
        
    for route in routes:
        direction, k = route.split(' ')
        if direction == 'E':
            d = [0, 1]
        elif direction == 'W':
            d = [0, -1]
        elif direction == 'S':
            d = [1, 0]
        elif direction == 'N':
            d = [-1, 0]
    
        init_h, init_w = h, w
        
        for i in range(int(k)):
            
            new_h, new_w = h+d[0], w+d[1]
            
            if (new_h >= len(park)) or (new_w >= len(park[0])):
                h, w = init_h, init_w
                break
            elif park[new_h][new_w] == 'X':
                h, w = init_h, init_w
                break
            elif (new_h < 0) or (new_w < 0):
                h, w = init_h, init_w
                break
            else:
                h, w = new_h, new_w
    answer = [h, w]
    return answer
