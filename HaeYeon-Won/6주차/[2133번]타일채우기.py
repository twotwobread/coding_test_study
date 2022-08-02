"""
문제
- 3xN 크기의 벽을 2x1, 1x2 크기의 타일로 채우는 경우의 수를 구하라
문제 유형
- 다이나믹 프로그래밍
자료구조
- list : dp정보 저장
사용한 아이디어
- n=2일때값을 a(2)라 하자
- 그림을 그려보면
- a(2)=3
- a(4) = 3*a(2)+2
- a(6) = 3*a(4)+2*a(2)+2
- a(8) = 3*a(6)+2*a(4)+2*a(2)+2 가 됨
- 이와 같은 형태로 계산해서 dp table을 채움
"""
def solution(n):
    if n%2!=0:
        return 0
    dp = [0 for _ in range(16)] # 1번 idx => 실제 2번 idx
    if n ==2:
        return 3
    dp[1]=3
    for i in range(2,16):
        dp[i]+=(3*dp[i-1]+2)
        pointer = i-2
        while pointer>=1:
            dp[i]+=(2*dp[pointer])
            pointer-=1
        if i==n//2:
            return dp[n//2]

if __name__ =="__main__":
    n = int(input())
    print(solution(n))