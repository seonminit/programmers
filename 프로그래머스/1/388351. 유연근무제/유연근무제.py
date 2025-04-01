def solution(schedules, timelogs, startday):
    answer = 0
    
    for idx in range(len(schedules)):
        success = list()
        # 시간 세팅(50분 이상 -> hour+=1)
        time = str(schedules[idx])
        minutes = time[-2:]
        if int(minutes) >= 50:
            hour = str(int(time[:-2]) + 1)
            minutes = str(int(minutes)+10 - 60).zfill(2)
            print(minutes)
            schedule = int(hour+minutes)
        else: 
            schedule = schedules[idx] + 10
            
        logs = timelogs[idx]
        for log in logs:
            # 로그 확인
            if (startday < 6) and (log <= schedule):
                success.append(1)
            elif (startday < 6) and (log > schedule):
                success.append(0)
            elif startday >= 6: 
                pass
            
            # 요일 변동
            if startday == 7:
                startday = 1
            else: 
                startday += 1 
        # 성공 여부        
        if min(success) == 1:
            answer += 1
        else:
            pass 
        
            
    return answer