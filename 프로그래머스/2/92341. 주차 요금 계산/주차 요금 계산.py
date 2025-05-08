import math
from collections import deque, defaultdict #helped by GPT

def solution(fees, records):
    answer = []
    arr = []
    dic = defaultdict(int)
    for record in records:
        record = record.split(' ')
        arr.append(record)
    deq = deque(arr)

    
    while deq:
        
        car_in = deq[0]
        if car_in[2] == 'OUT': #덱의 첫번째 차량의 상태가 OUT인 경우는 이미 계산이 끝난 경우이므로 popleft
            deq.popleft()
            continue
            
        out_find = False #출차 기록을 찾았음을 표현하는 플래그 초기화
        for j in range(1,len(deq)):
            car_out = deq[j]
            car_in_time = 0
            car_out_time = 0
            if car_in[1] == car_out[1] and car_out[2] == 'OUT': #치량 번호가 같고, 출차기록을 찾았을 때
                time = 0 #time 초기화
                out_find = True #출차 기록을 찾았음을 표현하는 플래그
                car_in_time = int(car_in[0][:2]) * 60 + int(car_in[0][3:]) #입차 시간 (분으로 환산 계산)
                car_out_time = int(car_out[0][:2]) * 60 + int(car_out[0][3:]) #출차 시간 (분으로 환산 계산)
                time = car_out_time - car_in_time #주차한 시간
                dic[car_in[1]] += time #딕셔너리에 주차한 시간 더해주기 (누적합을 위함)
                deq.popleft() #덱에서 빼주기
                break
                    
        if not out_find: #위의 for문을 돌았는데 입차 기록만 있고, 출차 기록이 없을 때
            time = 0
            car_in_time = int(car_in[0][:2]) * 60 + int(car_in[0][3:]) #입차 시간 계산
            time = 1439 - car_in_time #23:59 = 1439에서 입차 시간을 빼서 계산
            dic[car_in[1]] += time
            deq.popleft()
            
    #helped by GPT
    res_dic = dict(sorted(dic.items()))
    for k,v in res_dic.items():
        res = 0
        if v > fees[0]:
            res = fees[1] + math.ceil((v-fees[0])/fees[2]) * fees[3]
            answer.append(res)
        else:
            answer.append(fees[1])
        
    
    return answer