def solution(data):
    distance = data[1]-data[0]
    if distance==1: return 1
    elif distance==2: return 2
    start, end = 3, 4
    result=3
    step=2
    loop=1
    while True:
        if start<=distance<=end: return result
        start=end+1
        end=end+step
        result+=1
        loop+=1
        if loop==2:
            loop=0
            step+=1


if __name__ =="__main__":
    case = int(input())
    for _ in range(case):
        data = list(map(int, input().split()))
        print(solution(data))