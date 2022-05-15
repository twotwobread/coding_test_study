from collections import deque
def init(n,m,data):#초기 토마토 위치 파악
    result = deque()
    for i in range(n):
        for j in range(m):
            if data[i][j]==1:
                result.append((i,j))
    return result

def ans(n,m,data):
    result = 0
    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                print(-1)
                return
            result = max(result, data[i][j])
    print(result-1)
    return

def solution(n,m,data):
    direction = ((1,0),(0,1),(-1,0),(0,-1))
    q = init(n,m,data)
    while q:
        row, col = q.popleft()
        for dy, dx in direction:
            y, x = row+dy, col+dx
            if 0<=y<n and 0<=x<m:
                if data[y][x]==0: #아직 익지 않은 토마토인 경우
                    q.append((y,x))
                    data[y][x] = data[row][col]+1 #이전 깊이+1
    ans(n,m,data)

if __name__ =="__main__":
    m,n = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    solution(n,m,data)

"""
문제 
- 1은 익은 토마토, 0은 익지않은 토마토, -1은 갈 수 없는 곳
- 토마토가 전부 익지 못하는 경우도 있다
- https://www.acmicpc.net/problem/7576
- 골드 5
문제 유형 
- DFS / BFS : 깊이를 더해가며 진행하는 방식, 갈수 있는 방향으로 쭉가면 되서 위와같이 선정
자료구조 
- 2차원 리스트 : map 정보를 담기위해 사용
- deque : 현재 이동하고 있는 칸의 정보를 담기위해 사용. 리스트 보다 pop 속도가 빨라서 사용
- tuple : 방향 정보 저장
사용한 아이디어
- BFS 문제
- 초기에 익은 토마토 들을 deque에 담아주고 진행
- 만약 진행시 data가 0이라면 방문직전 깊이+1로 해당값을 갱신해 주었음
- 토마토가 다 익지 못한 경우도 있으므로 익지 않은 토마토가 있는경우 -1, 아닌경우 2차원 mtrx에서 최대값을 출력
"""
