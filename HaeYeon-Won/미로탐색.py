from collections import deque
def init(n,m,data):#문자열을 정수로 변환한 리스트 만들기
    result = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp. append(int(data[i][j]))
        result.append(temp)
    return result

def solution(n,m,data):
    direction = ((1,0),(0,1),(-1,0),(0,-1))
    q = deque([(0,0)])
    data = init(n,m,data)
    while q:
        row, col = q.popleft()
        for dy, dx in direction:
            y, x = row+dy, col+dx
            if 0<=y<n and 0<=x<m:
                if data[y][x]==1: #가보지 않은 방향만 이동
                    q.append((y,x))
                    data[y][x] = data[row][col]+1 #이전 깊이+1
    print(data[n-1][m-1])


if __name__ =="__main__":
    n,m = map(int, input().split())
    data = [list(input()) for _ in range(n)]
    solution(n,m,data)

"""
문제 
- 미로 탐색, 1은 이동가능 0은 이동 불가, count에 시작점과 끝점도 포함
- https://www.acmicpc.net/problem/2178
- 실버 1

문제 유형 
- DFS / BFS : 깊이를 더해가며 진행하는 방식, 갈수 있는 방향으로 쭉가면 되서 위와같이 선정

자료구조 
- 2차원 리스트 : map 정보를 담기위해 사용
- deque : 현재 이동하고 있는 칸의 정보를 담기위해 사용. 리스트 보다 pop 속도가 빨라서 사용
- tuple : 방향 정보 저장

사용한 아이디어
- 기본적인 BFS 문제
- data가 1인 곳은 아직 가보지 않은 곳이므로 data가 1인 경우에만 방문
- 방문 시 바로 직전값 + 1로 해당값을 갱신해 주어 최소 거리 계산
"""