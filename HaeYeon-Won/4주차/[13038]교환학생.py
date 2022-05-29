def solution(round, days, plan, num_lesson, start):
    global result 
    if start==-1:
        for i in range(7):
            if plan[i]:
                solution(round, days, plan,num_lesson, i)
        return
    else:
        temp =0
        while days!=0:
            if plan[start]:
                days-=1
            temp+=1
            start=(start+1)%7
        result = min(result, temp)
        return
if __name__ =="__main__":
    T = int(input())
    for round in range(1, T+1):
        result = 1e9
        days = int(input())
        plan = list(map(int, input().split()))
        num_lesson = plan.count(1)
        solution(round, days, plan, num_lesson, -1)
        print("#{} {}".format(round, result))