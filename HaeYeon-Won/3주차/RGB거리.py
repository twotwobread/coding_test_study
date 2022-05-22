
def solution(n, data):
    INF = 1e9
    dp = [[INF for _ in range(3)] for _ in range(n)]
    dp[0][0], dp[0][1], dp[0][2] = data[0][0], data[0][1], data[0][2]
    for i in range(n-1):
        for j in range(3):
            dp[i+1][j]=min(dp[i][(j-1)%3]+data[i+1][j],dp[i][(j+1)%3]+data[i+1][j]) #지금 j번쨰 색을 골랐다면 이전꺼는 (j-1)%3 or (j+1)%3을 고름
    print(min(dp[-1]))


if __name__=="__main__":
    n=int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    solution(n ,data)

"""
문제 
- N개의 집이 있음, 집은 RGB중 하나로 칠해야함.
- 1번집 색은 2번과 같지 않아야함
- N번집 색은 N-1번째 집의 색과 달라야함.
- 이때 최소 가격?
문제 유형 
- 다이나믹 프로그래밍
자료구조 
- 1차원 리스트 : 기존값 저장, 갱신값 저장에 사용
사용한 아이디어
- 다음칸에는 중복된 색상을 고를 수 없으므로 지금 j번쨰 색을 골랐다면 이전꺼는 (j-1)%3 or (j+1)%3을 고름
"""
