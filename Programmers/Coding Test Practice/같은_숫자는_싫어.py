def solution(arr):
    
    answer = []

    previous_temp = 999999
    for i in arr:
        if i == previous_temp:
            pass
        else:
            answer.append(i)
        previous_temp = i      
    return answer
