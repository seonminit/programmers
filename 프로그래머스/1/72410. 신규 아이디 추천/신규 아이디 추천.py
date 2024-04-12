import re 

def solution(new_id):

    # 1
    new_id = new_id.lower()
    # 2
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    # 3
    new_id = re.sub('[.]+', '.', new_id)
    # 4
    if (len(new_id) != 0 and new_id[0] == '.'):
        new_id = new_id[1:]
    if (len(new_id) != 0 and new_id[-1] == '.'):
        new_id = new_id[:-1]
    # 5
    if len(new_id) == 0:
        new_id = "a"
    # 6
    elif len(new_id) > 15:
        new_id = new_id[:15]
        new_id = re.sub('[.]$', '', new_id)
    else:
        pass
    # 7
    while len(new_id) < 3:
        new_id = new_id + new_id[-1]
    
    answer = new_id

    return answer