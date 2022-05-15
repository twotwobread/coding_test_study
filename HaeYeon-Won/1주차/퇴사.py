def backtracking(n, depth ,data, val):
    global ans
    if depth>n: #지정된 날을 넘어가면 쓸모없는 정보
        return
    ans = max(ans, val) #그게 아니라면 지금까지 번 돈의 최대를 설정
    for i in range(depth, n):#일하는 날 동안은 다른일을 못하므로 일이 끝난날을 시작점으로
        day, pay = data[i][0], data[i][1] #일하는 걸리는날, 버는 돈
        backtracking(n, i+day, data, val+pay)#현재일+걸리는 시간, 총 번돈을 전달

def dynamic(n,data):
    dp = [0 for _ in range(n+1)]
    for i in range(n):
        day, pay = data[i]
        after = i+day
        if after<=n:
            # 현재값과 바로 직전값중 더 큰값을 선정(지금까지 pay의 누적합이므로),0번 인덱스 일때는 dp[-1]을 찍어서 상관없음
            dp[i] = max(dp[i], dp[i - 1])
            # 현재까지의 누적값과, i번째 값+pay중 더 많이 벌 수 있는것을 선택
            dp[after]=max(dp[after], dp[i]+pay)
    dp.sort()
    print(dp[-1])


if __name__ =="__main__":
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    backtracking(n, 0,  data, 0)
    print(ans)
    dynamic(n,data)


"""
문제 
- N+1일째 되는날 퇴사 예정, N일 동안 최대한 많은 상담을 하려함
- https://www.acmicpc.net/problem/14501
- 실버 3
문제 유형 
- 그리디, dp, 입력 제한이 (1<=N<=15)개이므로 백트래킹도 가능할 듯
자료구조 
- 1차원 리스트(dp 테이블 생성을 위해 사용)
사용한 아이디어
- 상담에 걸리는 시간 : day, 버는돈 : pay
- 현재일까지의 누적합+pay 와 현재일+day 날의 누적합 중 큰 값을 선택
- dp로 풀이 시 dp table의 범위를 넘어가는 값은 사용 불가한 값이므로 무시
- 계산 중 누적합을 계속 업데이트 하기 위해 dp[i] = max(dp[i], dp[i-1]) 해줌
"""
